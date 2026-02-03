import re

def evaluate_password(password):
    suggestions = []

    # Length Check
    if len(password) < 8:
        suggestions.append("Your password could be extended (Aim for 8+ characters)")

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
    
    results = evaluate_password(user_pass)
    issue_count = len(results)

    print("\n--- Results ---")

    # Strength Rating Logic
    if issue_count == 0:
        print("Strength: STRONG")
        print("[+] Your password meets all security requirements!")
    elif issue_count == 1:
        print("Strength: GOOD")
    elif issue_count == 2:
        print("Strength: WEAK")
    else:
        # Handles 3 or more issues
        print("Strength: VERY WEAK")

    # Print the specific suggestions regardless of the tier
    if results:
        print("\nSuggestions to improve:")
        for suggestion in results:
            print(f"[!] {suggestion}")

    print("\nEvaluation completed.")