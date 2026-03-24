#!/usr/bin/python3

import random
import string

def generate_password(length):
    """
    Generate a random password of specified length.
    
    Args:
        length (int): Length of the password
        
    Returns:
        str: Generated password containing uppercase, lowercase, digits, and special characters
    """
    if length < 4:
        length = 4
    
    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure at least one character from each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest randomly
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)


def main():
    print("=== Password Generator ===\n")
    
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        
        if length < 4:
            print("Password length must be at least 4. Setting to 4.")
            length = 4
        
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
        
    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
