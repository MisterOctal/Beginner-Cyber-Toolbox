# Function to perform Caesar cipher encryption/decryption
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # For decryption reverse the shift
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            start = ord('A') if char.isupper() else ord('a')
            # The Formula: (Original Position + Shift - Start) % 26 + Start
            result += chr((ord(char) + shift - start) % 26 + start)
        else:
            # Preserve spaces, numbers, and punctuation
            result += char
    return result

# Function to perform brute-force attack on Caesar cipher
def brute_force(text):
    print("\n--- Starting Brute-Force Attack ---")
    for shift in range(1, 26):
        decrypted = caesar_cipher(text, shift, mode='decrypt')
        print(f"Shift {shift:2}: {decrypted}")

if __name__ == "__main__":
    print("--- Caesar Cipher Tool ---")
    choice = input("Select Mode: [E]ncrypt, [D]ecrypt, [B]rute-force: ").lower()
    
    message = input("Enter your message: ")

    if choice in ['e', 'd']:
        try:
            key = int(input("Enter shift key (1-25): "))
            mode_name = "encrypt" if choice == 'e' else "decrypt"
            output = caesar_cipher(message, key, mode_name)
            print(f"\nResult: {output}")
        except ValueError:
            print("[-] Error: Shift key must be a number.")
            
    elif choice == 'b':
        brute_force(message)
    else:
        print("[-] Invalid choice.")