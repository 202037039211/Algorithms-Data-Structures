def convert_to_snake_case(pascal_or_camel_cased_string):
    # Convert each uppercase character to lowercase and prefix with an underscore
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the list into a string and remove leading underscore if present
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Example test case: convert PascalCase to snake_case
    print(convert_to_snake_case('IAmAPascalCasedString'))  # Expected output: 'i_am_a_pascal_cased_string'

main()
