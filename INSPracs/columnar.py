def CCT_Enc(plain_text, key):
    new_text = ''
    for i in plain_text:
        new_text = new_text+(chr(ord(i)+key))
    print("Cipher text of Caesar Cipher is " + new_text)
    return new_text


def CCT_Dec(cypher_text, key):
    plain_text = ''
    for i in cypher_text:
        plain_text = plain_text+(chr(ord(i)-key))
    print("Decrypted text of Caesar Cypher is " + plain_text)


def ColTT_Enc(plain_text, key):
    matrix = []
    for i in range(key):
        matrix.append([])
    for i in range(len(plain_text)):
        matrix[i % key].append(plain_text[i])
    for i in matrix:
        print(i)
    cypher_text = ''
    for i in matrix:
        for char in i:
            cypher_text += char
    print("Cipher text of Columnar Transposition is " + cypher_text)
    return cypher_text


def ColTT_Dec(cypher_text, key):
    matrix = []
    for i in range(key):
        matrix.append([])
    count = int(len(cypher_text)/key)
    length = 0
    extra = int(len(cypher_text) % key)
    for charlist in matrix:
        for j in range(count):
            charlist.append(cypher_text[length])
            length = length+1
        if (extra != 0):
            charlist.append(cypher_text[length])
            length = length+1
            extra = extra-1
    for i in matrix:
        print(i)
    plain_text = ''
    for i in range(key+1):
        for charlist in matrix:
            if i > len(charlist)-1:
                continue
            plain_text = plain_text + charlist[i]
    print("Decrypted text of Columnar Transposition is " + plain_text)


string = input("Enter a string:")
key = int(input("Enter key:"))
col = int(input("Enter column number:"))
print("Cypher Caesar")
c1 = CCT_Enc(string, key)
CCT_Dec(c1, key)
print("Columnar Transposition")
c2 = ColTT_Enc(string, col)
ColTT_Dec(c2, col)