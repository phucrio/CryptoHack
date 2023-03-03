from sympy.ntheory.residue_ntheory import discrete_log
from Crypto.Util.Padding import unpad,pad
import json
import codecs
import hashlib
from Crypto.Cipher import AES
from pwn import remote

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)
    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
      return plaintext.decode('ascii')

share_secret = 1614388563332122752098703510390923066134536457896374139538253423986871371903043504640865084326776078532097286698839936506357011746373743987728755240984142277415357031755980954699167699770980502561781192539972817602177232642236592991738651825453814512757268184485996400993023063448953845025666763383372150971254078321524118076521462541914412470870836095917351982635822570475022629063039275544222068196147017216270381647770767515316967190073946037040085829611624445
iv = "72abca4ba196bd3562acf269f8578551"
ciphertext = "c22ca2e6545abcec87fed18ba449944219e9556fae52ae7975567823e20cd451"

print(decrypt_flag(share_secret,iv,ciphertext))