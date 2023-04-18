import math

def enc(plain,e,n):
    return (plain**e)%n

def dec(cipher,d,n):
    return (cipher**d)%n

def get_public_key(phi):
    e = 2
    while e < phi:
        if math.gcd(e,phi) == 1:
            break
        else:
            e += 1
    return e

def get_private_key(e,phi):
    d = 2
    while d < phi:
        if (d*e)%phi == 1:
            break
        else:
            d += 1
    return d

if __name__=='__main__':
    p,q = input('Enter two prime numbers: ').split()
    plain = int(input('Enter the plain text: '))
    p,q = int(p),int(q)
    n = p*q
    phi = (p-1)*(q-1)
    e = get_public_key(phi)
    d = get_private_key(e,phi)
    print('Public key(e,n): ',e,n)
    print('Private key(d,n): ',d,n)
    cipher = enc(plain,e,n)
    print('Cipher text: ',cipher)
    print('Plain text: ',dec(cipher,d,n))