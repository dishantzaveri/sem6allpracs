import numpy as np

def normalize_text(x,n):
    newx=x
    p = len(x)%n
    for i in range(p):
        newx+="x"
    return newx

def encrypt(x,mat,n):
    if len(x)%n!=0:
        new_x = normalize_text(x,n)
    else:
        new_x=x
    cipher=""
    for i in range(0,len(new_x),n):
        temp=[]
        for j in range(n):
            temp.append(ord(new_x[i+j])-ord('a'))
        sol=np.dot(mat,temp)
        for j in sol:
            cipher+=chr((j%26)+ord('a'))
    return cipher
def decrypt(cipher,mat,n):
    text=""
    det=round(np.linalg.det(mat))
    new_det = pow(det,-1,26)
    adjoint = (np.linalg.inv(mat)*det)
    new_adj=[]
    for i in range(len(adjoint)):
        temp=[]
        for j in range(len(adjoint[i])):
            if adjoint[i][j]<0:
                temp.append((round(adjoint[i][j])+26)*new_det)
            else:
                temp.append(round(adjoint[i][j])*new_det)
            
        new_adj.append(temp)

    text = encrypt(cipher,new_adj,n)
    return text


def main():
    x="attack"
    n=2
    mat=[[2,3],[3,6]]
    print(mat)
    cipher = encrypt(x,mat,n)
    print("Encrypted Text: ",cipher)
    print()
    x_ = decrypt(cipher,mat,n)
    print("Decrypted Text: ",x_)
main()