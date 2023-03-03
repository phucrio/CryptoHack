import requests
import json
def strxor(a, b):     
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

url = 'http://aes.cryptohack.org/'
ciphertext = '4cb41a0b195511fcedd88a9c9eb05f50539210d06d39020b8317081444e8a64bfe2e2361b959a1d293229e3c7b590f7d'
iv = bytes.fromhex(ciphertext[:16])
cipher = bytes.fromhex(ciphertext[16:])
r = requests.get(url+'ecbcbcwtf/decrypt/4cb41a0b195511fcedd88a9c9eb05f50539210d06d39020b8317081444e8a64bfe2e2361b959a1d293229e3c7b590f7d/')
data = r.json()
p_0 = bytes.fromhex(data['plaintext'][:16])
p_1 = bytes.fromhex(data['plaintext'][16:])

actual1 = strxor(iv, p_0)
actual2 = strxor(cipher[:16], p_1)

print(f'{iv = }')
print(actual1+actual2)
print(p_1.hex())