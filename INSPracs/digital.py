import hashlib

def gcd(a , b):
  while b != 0:
    a , b = b , a % b
  return a

def encrypt(key , pt):
  a , b = key 
  return pow(pt,a,b)

def decryption(key , ct):
  a , b = key
  return pow(ct,a,b)

if __name__ == "__main__":
  p = int(input("Enter value of p : "))
  q = int(input("Enter value of q : "))
  n = p * q
  phi = (p-1)*(q-1)
  e = 2
  while gcd(e , phi) != 1:
    e += 1
  d = pow(e,-1,phi)
  # sender side
  msg= input("Enter plain text : ")
  plain_text  = bytes(msg,'utf-8')

  hash_value = hashlib.sha256(plain_text).hexdigest()
  hash_value = int(hash_value, 16) % n
  print("Hash value at sender end: ", hash_value)
  
  signature = encrypt((d,n),hash_value)
  print("Digital signature: ", signature)
  
  # receiver side 
  hash_value_check = decryption((e,n), signature)
  print("Hash value checked at receiver end: ", hash_value_check)
  if hash_value_check == hash_value:
      print("Verified")
  else:
      print("Not verified")