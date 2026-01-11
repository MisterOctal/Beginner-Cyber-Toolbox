import re

def evaluate_password(password):
    """
    Checks the password against complexity rules and returns a list of suggestions.
    """
    suggestions = []

    # Length Check
    if len(password) < 12:
        suggestions.append("Your password could be extended (Aim for 12+ characters)")

    # Upper and Lower Case Check
    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        suggestions.append("Your password should contain upper and lower case")

    # Numbers Check
    if not re.search(r"\d", password):
        suggestions.append("Your password should contain at least one number")

    # Special Character Check
    if not re.search(r"[!@#$%^&*(),.?\":{}|<> ]", password):
        suggestions.append("Your password should contain special characters")

    return suggestions

if __name__ == "__main__":
    print("--- Password Complexity Auditor ---")
    user_pass = input("Enter a password to evaluate: ")
    
    # Run the evaluation
    results = evaluate_password(user_pass)

    print("\n--- Results ---")
    if not results:
        # If the list is empty, it means all checks passed
        print("[+] Your password is perfect!")
    else:
        # Loop through and print each suggestion found
        for suggestion in results:
            print(f"[!] {suggestion}")

    print("\nEvaluation completed.")