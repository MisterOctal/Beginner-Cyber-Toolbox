import hashlib
import os
import sys

# Function to calculate the SHA-256 hash of a file
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        # Open file in binary mode for hashing
        with open(filepath, "rb") as f:
            # Read in chunks to efficiently handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except PermissionError:
        print(f"Error: Permission denied for file '{filepath}'.")
        return None

# Function to manage the baseline and integrity check logic
def run_integrity_checker():
    print("--- File Integrity Checker ---")
    target_file = input("Enter the path of the file to monitor: ")

    # Validate file existence
    if not os.path.exists(target_file):
        print(f"Error: Target file '{target_file}' not found.")
        return

    baseline_file = "baseline.txt"

    print("\nModes:")
    print("[1] Generate Baseline (Save current file hash)")
    print("[2] Check Integrity (Compare current hash against baseline)")
    choice = input("Select Mode: ")

    if choice == '1':
        # Mode 1: Create a known-good hash
        hash_value = calculate_hash(target_file)
        if hash_value:
            with open(baseline_file, "w") as f:
                f.write(hash_value)
            print(f"Baseline established. Hash saved to {baseline_file}")

    elif choice == '2':
        # Mode 2: Verify if the file has changed
        if not os.path.exists(baseline_file):
            print("Error: No baseline file found. Please run Mode 1 first.")
            return

        with open(baseline_file, "r") as f:
            stored_hash = f.read().strip()

        current_hash = calculate_hash(target_file)

        print("\n--- Integrity Results ---")
        if current_hash == stored_hash:
            print("SUCCESS: File integrity verified. No changes detected.")
        else:
            print("ALERT: File has been ALTERED or TAMPERED with!")
            print(f"Expected: {stored_hash}")
            print(f"Actual:   {current_hash}")

    else:
        print("Error: Invalid selection.")

if __name__ == "__main__":
    try:
        run_integrity_checker()
    except KeyboardInterrupt:
        print("\nTool stopped by user.")
        sys.exit()

    print("\nTask completed.")