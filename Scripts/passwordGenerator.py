import random
import string
import sys

# Function to generate a secure password
def generate_password(length):
    # Define our character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # 1. Force at least one character from each category
    # This ensures the password isn't just "aaaaaaaa"
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # 2. Fill the remaining length with random choices from ALL categories
    all_characters = lower + upper + digits + special
    
    # We subtract 4 because we already added 4 characters above
    for _ in range(length - 4):
        password_chars.append(random.choice(all_characters))

    # 3. Shuffle the list so the first 4 characters aren't predictable
    random.shuffle(password_chars)
    
    # Join the list into a string and return it
    return "".join(password_chars)

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    
    while True:
        try:
            user_input = input("Enter password length (min 8): ")
            length = int(user_input)

            if length < 8:
                print("[-] Error: For security, length must be at least 8.")
            else:
                # Generate and display
                password = generate_password(length)
                print(f"\n[+] Generated Password: {password}")
                
                # Option to generate another or exit
                again = input("\nGenerate another? (y/n): ").lower()
                if again != 'y':
                    break
                    
        except ValueError:
            print("[-] Error: Please enter a number.")
        except KeyboardInterrupt:
            print("\nTool stopped by user.")
            sys.exit()

    print("\nTask completed.")