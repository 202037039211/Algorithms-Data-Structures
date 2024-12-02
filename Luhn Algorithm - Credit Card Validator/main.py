def verify_card_number(card_number):
    sum_of_odd_digits = 0
    
    # Reverse the card number for easier processing from the right
    card_number_reversed = card_number[::-1]
    
    # Extract odd-position digits (1st, 3rd, etc., in reversed order)
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)  # Sum these digits directly

    sum_of_even_digits = 0
    
    # Extract even-position digits (2nd, 4th, etc., in reversed order)
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2  # Double the digit
        
        # If the result is two digits, sum those digits (e.g., 12 -> 1 + 2 = 3)
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        sum_of_even_digits += number  # Add to the even digit sum
    
    # Calculate total and check if it is divisible by 10
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'  # Example credit card number
    
    # Remove hyphens and spaces for processing
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Validate the card number using the Luhn algorithm
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
