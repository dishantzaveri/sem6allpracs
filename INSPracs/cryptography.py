def p_expansion(rp):
    new_rp = ""
    new_rp += rp[1]+rp[2]+rp[3] + rp[1]+rp[2]+rp[0] +rp[3]
    return new_rp


def s_compression(val):
    box_no = int(val[0:2], 2)
    row_no = int(val[2:5], 2)
    col_no = int(val[5:7], 2)
    new_val = abs(row_no*col_no-box_no*5) % 15
    new_val=format(new_val,'b')
    return new_val


def mixer(rp, key):
    new_rp = p_expansion(rp)
    print('p expansion: ',new_rp)
    temp = int(key,2) ^ int(new_rp,2)
    temp=format(temp,'b')
    if len(temp)<7:
      temp='0'*(7-len(temp))+temp
    print('xor: ',temp)
    new_rp = s_compression(temp)
    print('s compression: ',new_rp)
    return new_rp


def my_encrypt(plain, key):
    if len(plain) % 8 != 0:
        plain += '*'*(8-plain % 8)
    n = int(len(plain)/8)
    for i in range(0, n):
        lp = plain[0+i*4:4+i*4]
        rp = plain[4+i*4:8+i*4]
        print('lp: ',lp,' rp: ',rp)
        mixer_val = mixer(rp, key)
        new_rp = int(lp,2) ^ int(mixer_val,2)
        new_rp=format(new_rp,'b')
        if len(new_rp)<4:
          new_rp='0'*(4-len(new_rp))+new_rp
        cipher=rp+new_rp
        print('cipher: ',cipher)
        return cipher
        
def my_decrypt(cipher, key):
    n = int(len(cipher)/8)
    for i in range(0, n):
        lp = cipher[0+i*4:4+i*4]
        rp = cipher[4+i*4:8+i*4]
        og_rp=lp
        print('lp: ',lp,' rp: ',rp)
        mixer_val = mixer(og_rp, key)
        new_lp = int(rp,2) ^ int(mixer_val,2)
        new_lp=format(new_lp,'b')
        decipher=new_lp+og_rp
        print('decipher: ',decipher)
        

plain = input("enter plain text:")
key = input("enter key:")
cipher=my_encrypt(plain, key)
print()
my_decrypt(cipher,key)

# 10111001
# 1010101