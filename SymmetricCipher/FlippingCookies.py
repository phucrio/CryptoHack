from Crypto.Util.number import *
import requests
import json
from pwn import xor

def get_ciphertext():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/"
    r = requests.get(url)
    ct = (json.loads(r.text))['cookie']
    return ct

def check_cookie(cookie, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"+cookie+"/"+iv
    r = requests.get(url)
    try:
        flag = (json.loads(r.text))['flag']
    except:
        flag = (json.loads(r.text))['error']
    return flag

c = get_ciphertext()
iv = bytes.fromhex((c[:32]))
ct = c[32:]
print("iv = %s" % iv.hex())
print("ct = %s" % ct)
iv1 = xor(iv,b'admin=False',b'admin=True;').hex()
print("iv1 = %s" % iv1)
flag = check_cookie(ct, iv1)
print(flag)