import random
import string

def get_char(n):
  return chr(n + 97)

def left_rotate(s , n):
  return s[n:] + s[:n]

def right_rotate(s , n):
  n = n % len(s)
  return s[-n:] + s[:-n]

def get_index(s):
  return ord(s.lower()) - 97

def sbox_substitution(s):
  return get_char((get_index(s[0])-3)%26) +get_char((get_index(s[1])+3)%26)

def rev_sbox_substitution(s):
  return get_char((get_index(s[0])+3)%26) +get_char((get_index(s[1])-3)%26)

def pbox_permutation(s):
  s_list = list(s)
  n = len(s_list)
  i = 0
  j = n - 1
  while i < j:
    s_list[i] , s_list[j] = s_list[j] , s_list[i]
    i += 2
    j -= 2
  return "".join(s_list)

def encryption(pt):
  n = len(pt)
  pt = left_rotate(pt , 3)
  half = int(n/2)
  LPT = pt[:half]
  RPT = pt[half:]
  key = ''.join(random.choices(string.ascii_lowercase,k=len(LPT)))
  temp_LPT = ""
  print(key)
  print("Before xor : ",LPT)
  for i in range(len(LPT)):
    temp = get_index(LPT[i]) ^ get_index(key[i])
    temp_LPT += get_char(temp%26)
    print(f"{get_index(LPT[i])} ^ {get_index(key[i])} ={temp}")
  LPT = temp_LPT
  i = 0
  j = 1
  temp_LPT = ""
  print("Before s : ",LPT)
  while i < len(LPT):
    temp_LPT += sbox_substitution(LPT[i:j+1])
    i += 2
    j += 2
  LPT = temp_LPT
  print(LPT)
  LPT = pbox_permutation(LPT)
  print(RPT)
  RPT = pbox_permutation(RPT)
  ct = LPT + RPT
  return key , ct

def decryption(ct , key):
  print(ct)
  n = len(ct)
  half = int(n/2)
  LPT = ct[:half]
  RPT = ct[half:]
  RPT = pbox_permutation(RPT)
  LPT = pbox_permutation(LPT)
  i = 0
  j = 1
  temp_LPT = ""
  while i < len(LPT):
    temp_LPT += rev_sbox_substitution(LPT[i:j+1])
    i += 2
    j += 2
  LPT = temp_LPT
  temp_LPT = ""
  print(LPT)
  for i in range(len(LPT)):
    temp = get_index(LPT[i]) ^ get_index(key[i])
    temp_LPT += get_char(temp%26)
    print(f"{get_index(LPT[i])} ^ {get_index(key[i])} ={temp}")
  LPT = temp_LPT
  print(LPT + RPT)
  pt = right_rotate(LPT + RPT , 3)
  return pt

if __name__ == "__main__":
  # plain_text = input("Enter plain text : ")
  plain_text = "djsaghvi"
  # print(sbox_substitution("jp"))
  key ,ct = encryption(plain_text)
  print("Encrypted",ct)
  print("Decrypted",decryption(ct ,key))

#  Get a plain text
#  For initial permutation left rotate string by half
#  divide plain text into two parts LPT and RPT
#  generate key of size LPT and perform XOR with LPT
#  now perform s-box substitution where for every two characters replace left character with
# it’s index - 3rd position character and for right character replace it with it’s index + 3
# character
#  finally perform P-box permutation where replace first character with last character skip
# 2nd and 2nd last character , replace third and third last character and skip 4th and 4th last
# character continue for entire string
#  finally combine LPT and RPT