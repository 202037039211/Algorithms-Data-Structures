import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define character sets
    letters = string.ascii_letters          # All uppercase and lowercase letters
    digits = string.digits                  # All numeric digits (0-9)
    symbols = string.punctuation            # All special characters (!@#$, etc.)
    
    all_characters = letters + digits + symbols  # Combine all characters into a pool

    while True:
        password = ''.join(secrets.choice(all_characters) for _ in range(length))  # Generate a random password
        
        # Define the constraints with regular expressions
        constraints = [
            (nums, r'\d'),                    # At least `nums` digits
            (special_chars, fr'[{symbols}]'), # At least `special_chars` special characters
            (uppercase, r'[A-Z]'),            # At least `uppercase` uppercase letters
            (lowercase, r'[a-z]')             # At least `lowercase` lowercase letters
        ]

        # Validate constraints: Ensure the password meets all criteria
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break  # Stop if all constraints are satisfied
    
    return password  # Return the generated password
    
if __name__ == '__main__':
    new_password = generate_password()  # Generate and print the password
    print('Generated password:', new_password)
