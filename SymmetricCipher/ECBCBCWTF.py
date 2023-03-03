import requests
from pwn import xor

def get_ciphertext():
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    r = requests.get(url)
    data = r.json()
    ct = data['ciphertext']
    return ct

def decrypt_ecb(ct):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"+ct
    r = requests.get(url)
    data = r.json()
    pt = data['plaintext']
    return pt


ciphertext = get_ciphertext()
split_ciphertext = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]  
# [0] is the IV, [1] and subsequent are the encryptions of the plaintext blocks.

plaintext = ['']*(len(split_ciphertext) - 1)
for i in range(len(plaintext)):
    pi = bytes.fromhex(decrypt_ecb(split_ciphertext[i+1]))
    ci = bytes.fromhex(split_ciphertext[i])
    plaintext[i] = ''.join(map(chr, xor(pi, ci)))

print(f"Flag: {''.join(plaintext)}")