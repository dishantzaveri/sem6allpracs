def CCT_Enc(plain_text,key):
    new_text=''
    for i in plain_text:
        new_text = new_text+(chr(ord(i)+key))
    print(new_text)

def CCT_Dec(cypher_text,key):
    plain_text=''
    for i in cypher_text:
        plain_text = plain_text+(chr(ord(i)-key))
    print(plain_text)

def ColTT_Enc(plain_text,key):
    matrix = []
    for i in range(key):
        matrix.append([])
    for i in range(len(plain_text)):
        matrix[i%key].append(plain_text[i])
    for i in matrix:
        print(i)
    cypher_text = ''
    for i in matrix:
        for char in i:
            cypher_text+=char
            
    print(cypher_text)

def ColTT_Dec(cypher_text,key):
    matrix = []
    for i in range(key):
        matrix.append([])
    count = int(len(cypher_text)/key)
    length = 0
    extra = int(len(cypher_text)%key)
    for charlist in matrix:
        for j in range(count):
            charlist.append(cypher_text[length])
            length=length+1
        if(extra != 0):
            charlist.append(cypher_text[length])
            length=length+1
            extra = extra-1
    for i in matrix:
        print(i)
    plain_text = ''
    for i in range(key):
        for charlist in matrix:
            if i>len(charlist)-1:
               continue
            plain_text = plain_text +charlist[i]
    print(plain_text)
    
CCT_Enc('string',4)
CCT_Dec('wxvmrk',4)
ColTT_Enc('djsanghvi',4)
ColTT_Dec('dnijgshav',4)