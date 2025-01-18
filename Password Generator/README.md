# Password Generator

This project generates strong, customizable passwords with specified complexity rules.

## Features:
- **Random Password Generation:** Uses a secure random generator (`secrets` module).
- **Customizable Criteria:** Adjust password length, number of digits, special characters, etc.
- **Validation:** Ensures generated passwords meet the complexity requirements.

## Usage:
1. **Default Generation:** Run the script directly to generate a 16-character password.

2. **Customization:** Modify the `generate_password()` parameters:
```python
generate_password(length=20, nums=2, special_chars=3)
```
