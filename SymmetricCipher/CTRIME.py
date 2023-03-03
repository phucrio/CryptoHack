import requests
import json
import string

def encrypt(pt_hex):
    url = f"http://aes.cryptohack.org/ctrime/encrypt/{pt_hex}/"
    r = requests.get(url)
    try:
        enc = (json.loads(r.text))['ciphertext']
        return enc
    except:
        enc = (json.loads(r.text))
        return enc

flag = b'crypto{'
#c = encrypt(flag.hex())
#print(len(c))

while 1:
    c = encrypt(flag.hex())
    for i in string.printable:
        p = (flag+i.encode()).hex()
        l = len(encrypt(p))
        #print(l, i)
        n = len(c)
        if l == n:
            flag += i.encode()
            print(flag.decode())
            break
    if flag.endswith(b'M'):  
        flag += b'E'        
        print(flag.decode())
    '''Had to add this if statement because every printable gives the same length so guessed it would be "E" after "CRIM" '''
    if flag.endswith(b'}'):
        print(flag.decode())
        break