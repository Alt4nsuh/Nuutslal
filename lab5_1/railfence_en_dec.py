import numpy as np

def encrypt(str1, key):
    deckey = ""
    c = len(key)
    c1 = len(str1)
    arr = np.array(list(str1))
    padding = c - (c1 % c)
    if padding != c:
        arr = np.append(arr, [' '] * padding)

    newarr = arr.reshape(c1 // c + (1 if padding != c else 0), c)
    print("Encrypted 2D Matrix:")
    print(newarr)
    
    str3 = ""
    for i in range(1, len(key) + 1):
        index = key.index(str(i))
        str3 += "".join(newarr[:, index])
    return str3

def decrypt(str1, key):
    c = len(key)
    c1 = len(str1)
    arr = np.array(list(str1))

    newarr = np.zeros((c1 // c, c), dtype=str)
    print(arr.reshape(c,c1// c))
    
    k = 0
    for i in range(1, len(key) + 1):
        index = key.index(str(i))
        size = (c1 // c) if i > (c1 % c) else (c1 // c) - 1
        print(k)
        newarr[:size, index] = arr[k:k+size]
        k += size
    
    decrypted_message = "".join(newarr.flatten())
    return decrypted_message

# Example usage:
key = "4123567"
message = "attackpostponeduntiltwoamxyza"

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
