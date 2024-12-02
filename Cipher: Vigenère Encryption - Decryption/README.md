# Cipher: Vigenère Encryption/Decryption

This project implements the Vigenère cipher to encrypt and decrypt messages using a custom key.

## Functions:

### `vigenere(message, key, direction=1)`
- **Parameters**:
  - `message`: The text to encrypt or decrypt.
  - `key`: The encryption/decryption key.
  - `direction`: The direction of the cipher (1 for encryption, -1 for decryption).
- **Returns**: The encrypted or decrypted message.

### `encrypt(message, key)`
Encrypts the given message using the Vigenère cipher.

### `decrypt(message, key)`
Decrypts the given message using the Vigenère cipher.

## Example:

```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Encrypt the message
encrypted = encrypt(text, custom_key)

# Decrypt the message
decrypted = decrypt(encrypted, custom_key)

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
```
