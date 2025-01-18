# Credit Card Validator (Luhn Algorithm)

This project verifies credit card numbers using the Luhn algorithm, ensuring they adhere to common validation rules.

## How It Works:
- The card number is processed from right to left.
- Odd-positioned digits are summed directly.
- Even-positioned digits are doubled, and any results over 9 are split into their individual digits and summed.
- The total sum is checked: if divisible by 10, the card number is valid.

## Usage:
1. Set the `card_number` variable in the `main` function.
2. Run the script.
3. It prints "VALID!" if the card number is correct or "INVALID!" otherwise.

## Example:
- Input: `4111-1111-4555-1142`
- Output: `VALID!`

## License:
This project is licensed under the MIT License.
