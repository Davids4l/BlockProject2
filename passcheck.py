#!/usr/bin/env python3
import re
import sys
import getpass

# This function checks password based on certain criteria
def CheckPassword(password):
    
    #Evaluating password strength based on multiple criteria
    #Returns a score and feedback.
    score = 0
    goodFeedback = []
    badFeedback = []
    
    
    # Check length
    if len(password) >= 12:
        score += 3
        goodFeedback.append("Amazing length: 12+ characters")
    elif len(password) >= 8:
        score += 2
        goodFeedback.append("Decent length: 8-11 characters")
    else:
        badFeedback.append("Password is too short. Use >= 8 characters")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        goodFeedback.append("Contains at least one uppercase letter")
    else:
        badFeedback.append("Add uppercase letter(s) to password")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        goodFeedback.append("Contains at least one lowercase letter")
    else:
        badFeedback.append("Add lowercase letter(s) to password")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
        goodFeedback.append("Contains at least one number")
    else:
        badFeedback.append("Add number(s) to your password")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        goodFeedback.append("Contains at least one special character")
    else:
        badFeedback.append("Add special character(s) to your password")

    # More points for multiple special characters
    special_count = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password))
    if special_count >= 2:
        score += 2
        goodFeedback.append("Multiple special characters, great job!")
    
    # More points for multiple numbers
    number_count = len(re.findall(r'\d', password))
    if number_count >= 3:
        score += 2
        goodFeedback.append("Multiple numbers, great job!")
    
    # Check for common patterns
    common_patterns = ['password', '123456', 'abc123', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        score = max(0, score - 5)
        badFeedback.append("Uses a common password, susceptible to an attack")

    # Check for repeated characters, same character repeated 3+ times
    if re.search(r'(.)\1{2,}', password):
        score = max(0, score - 1)
        badFeedback.append("Avoid repeating characters")
    
    # Determine strength category
    if score >= 8:
        strength = "STRONG"
    elif score >= 5:
        strength = "DECENT"
    else:
        strength = "WEAK"
    
    return {
        'score': max(0, min(10, score)), #max score is 10 round down or up
        'strength': strength,
        'goodFeedback': goodFeedback,
        'badFeedback': badFeedback
    }

def main():
    # Main program function with user interaction
    print("\n" + "=============================")
    print("CHECK YOUR PASSWORD STRENGTH")
    print("\n !!! This tool is for educational purposes only !!!")
    print("\n!!! DO NOT enter real passwords into unofficial tools !!!")
    print("\n" + "=============================")
    
    while True:
        print("\n Enter one of the following:")
        print("1. Check password")
        print("2. Learn more about creating strong passwords")
        print("3. Exit")
        
        choice = input("\n Enter either 1,2, or 3: ").strip()
        
        if choice == '1':
            # getpass hides password input
            password = getpass.getpass("\nEnter password to check: ")
            
            # Checking password strength
            result = CheckPassword(password)
            
            # Display the results
            print(f"\n PASSWORD STRENGTH: {result['strength']}")
            print(f"SCORE: {result['score']}/10")
            print("\n Detailed Analysis:")
            
            if result['goodFeedback']: 
                print("\n What you did well:")
                for item in result['goodFeedback']:
                    print(f"  • {item}")

            if result['badFeedback']:
                print("\n Suggestions for improvement:")
                for item in result['badFeedback']:
                    print(f"  • {item}")

            if not result['goodFeedback'] and not result['badFeedback']:
                print("\n No specific feedback available.")
            
        elif choice == '2':
            print("\n" + "="*40)
            print("HOW TO CREATE STRONG PASSWORDS:")
            print("="*40)
            print("\n DO:")
            print("  • Use at least 12 characters")
            print("  • Mix uppercase, lowercase, numbers, and symbols")
            print("  • Add multiple numbers and symbols")
            print("\n DON'T:")
            print("  • Use personal info like birthdays or names")
            print("  • Use common words or patterns")
            print("  • Repeat the same characters more than twice")
        elif choice == '3':
            print("\n Goodbye! Stay safe.\n")
            sys.exit(0)
        else:
            print("\n Invalid choice, please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n An interrupt occured, bye bye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n  An error has occurred: {e}")
        print("Try again.")
        sys.exit(1)