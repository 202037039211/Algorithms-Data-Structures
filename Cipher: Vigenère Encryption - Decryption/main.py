# The message and custom key for encryption and decryption
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Function to perform Vigenère cipher encryption or decryption
def vigenere(message, key, direction=1):
    key_index = 0  # Index to track the position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Alphabet used for encryption
    final_message = ''  # Final result (encrypted or decrypted message)

    # Iterate over each character in the message
    for char in message.lower():
        # If the character is not a letter, append it as is
        if not char.isalpha():
            final_message += char
        else:
            # Find the corresponding character from the key
            key_char = key[key_index % len(key)]
            key_index += 1  # Move to the next character in the key

            # Define the shift (offset) based on the key character
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

# Function to encrypt the message
def encrypt(message, key):
    return vigenere(message, key)

# Function to decrypt the message (direction = -1 for decryption)
def decrypt(message, key):
    return vigenere(message, key, -1)

# Encrypting and decrypting the message
print(f'Encrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')

