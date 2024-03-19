import string


def encrypt(plaintext, key):
    encrypted_text = ""
    alphabet = string.ascii_lowercase

    for char in plaintext.lower():
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    decrypted_text = ""

    for char in ciphertext.lower():
        if char in key:
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char

    return decrypted_text

plaintext = "asdfghjkl"
key = "zyxwvutsrqponmlkjihgfedcba"

encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
