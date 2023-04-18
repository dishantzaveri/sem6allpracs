# RSA Improved

import random

def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_primes():
    """Generate 2 random prime numbers.
    We improve by generating very huge prime numbers to mitigate chosen cipher attack and factorization attack.
    This also mitigates the low decryption exponent attack"""
    primes = []
    a = 1 * 10 ** 10
    b = 9 * 10 ** 10
    while len(primes) < 2:
        num = random.randint(a, b) # generate a random number between 1 * 10 * 150 and 9 * 10 * 150
        if is_prime(num):
            primes.append(num)
    return primes

def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def find_e(phi):
    """Find an e such that gcd(e, phi) == 1."""
    for e in range(2, phi-1):
        if gcd(e, phi) == 1:
            return e
    return None

def gcd_extended(a, b):
    """
    Return a tuple (gcd, x, y) such that a*x + b*y = gcd,
    where gcd is the greatest common divisor of a and b.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = gcd_extended(b % a, a)
        return (gcd, y - (b // a) * x, x)

def find_d(e, phi):
    """
    Find an integer d such that (e * d) mod phi == 1,
    given e and phi.
    """
    gcd, x, _ = gcd_extended(e, phi)
    if gcd != 1:
        # e and phi are not coprime, so no solution exists
        return None
    else:
        # x is the multiplicative inverse of e modulo phi
        return x % phi

def public_private_key():
    p, q = generate_random_primes()
    # print(p, q)
    n = p*q
    phi = (p-1)*(q-1)
    e = find_e(phi)
    d = find_d(e, phi)
    if e is None or d is None:
        print("Encryption and Decryption not possible.")
    print(f'e: {e}\nd: {d}')
    return(e, d, n)

def encrypt(m, e, n):
    ct = pow(m, e, n)
    return ct

def decrypt(c, d, n):
    pt = pow(c, d, n)
    return pt

m = int(input("Enter the message to be encrypted: "))

# Finding public and private keys
e, d, n = public_private_key()

# Encryption c = (msg ^ e) % n
c = encrypt(m, e, n)
print("Encrypted data = ", c)

# Decryption m = (c ^ d) % n
p = decrypt(c, d, n)
print("Decrypted data = ", p)