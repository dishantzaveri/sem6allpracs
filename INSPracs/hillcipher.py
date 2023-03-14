import numpy as np

def hill_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % key.shape[0] != 0:
        plain_text += "X" * (key.shape[0] - len(plain_text) % key.shape[0])
    plain_text = np.array(list(plain_text)).reshape((-1, key.shape[0]))
    cipher_text = ""
    for block in plain_text:
        block_num = np.array([ord(ch) - 65 for ch in block])
        cipher_num = np.dot(key, block_num) % 26
        cipher_text += "".join([chr(int(num + 65)) for num in cipher_num])
    return cipher_text

def hill_decrypt(ciphertext, key):
    key_inverse = np.linalg.inv(key)
    key_det = np.round(np.linalg.det(key)).astype(int)
    det_inverse = 0
    for i in range(26):
        if (i * key_det) % 26 == 1:
            det_inverse = i
            break
   
    if det_inverse == 0:
        return None
    key_mod_inverse = np.mod(det_inverse * key_det * key_inverse, 26)
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    while len(ciphertext) % key.shape[0] != 0:
        ciphertext += 'X'
    blocks = [ciphertext[i:i+key.shape[0]] for i in range(0, len(ciphertext), key.shape[0])]
    plaintext = ''
    for block in blocks:
        block_indices = [ord(char) - ord('A') for char in block]
        block_matrix = np.array(block_indices).reshape(key.shape[0], -1)
        block_plaintext_matrix = np.mod(key_mod_inverse @ block_matrix, 26)
        block_plaintext_indices = block_plaintext_matrix.flatten().tolist()
        block_plaintext = ''.join([chr(int(index) + ord('A')) for index in block_plaintext_indices])
        plaintext += block_plaintext
    return plaintext
matrix = []
print("Enter the entries rowwise:")
for i in range(2):        
    a =[]
    for j in range(2):    
         a.append(int(input()))
    matrix.append(a)

key=np.array(matrix)
print(key)
plain_text = input("Enter text")
cipher_text = hill_encrypt(plain_text, key)
print(cipher_text)

decrypted_text = hill_decrypt(cipher_text, key)
print(f"decrypted text is {decrypted_text}")