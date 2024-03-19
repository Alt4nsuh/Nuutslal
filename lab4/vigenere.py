import string

def crypt(plaintext, key,i):
    a = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    for p, k in zip(plaintext.lower(), key_repeated.lower()):
        if p in a:
            p_index = a.index(p)
            k_index = a.index(k)
            encrypted_char = a[(p_index + i*k_index) % 26]
            encrypted_text += encrypted_char
        else:
            encrypted_text += p

    return encrypted_text

plaintext = "hello world"
key = "kedkjfdfkdsfkdgjy"

encrypted_text = crypt(plaintext, key,1)
print("Encrypted:", encrypted_text)

decrypted_text = crypt(encrypted_text, key,-1)
print("Decrypted:", decrypted_text)
