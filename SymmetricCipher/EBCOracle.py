from binascii import hexlify
import requests
import json
from string import printable

def encrypt(pt):
    p = hexlify(pt).decode()
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"+p
    r = requests.get(url)
    ct = (json.loads(r.text))['ciphertext']
    return ct


flag = "crypto{"
n = 31
while 1:
    payload = b'1'*(n-len(flag))
    comp = encrypt(payload)
    for i in printable:
        enc = encrypt(payload + flag.encode() + i.encode())
        if comp[32:64] == enc[32:64]:
            flag += i
            print("flag letter: ", i)
            break
    if flag[-1] == '}':
        break
print(flag)