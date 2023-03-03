from Crypto.Cipher import AES
import requests
import hashlib

res = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertext_hex = res.json()["ciphertext"]
with open('words', 'r') as f:
    for word in f:
        word = word.strip()
        attempted_key = hashlib.md5(word.encode()).hexdigest()
        ciphertext = bytes.fromhex(ciphertext_hex)
        key = bytes.fromhex(attempted_key)
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext)
            result = bytes.fromhex(decrypted.hex())
            if result.startswith('crypto{'.encode()):
                print("KEY : %s" % word)
                print("Flag: %s" % result.decode())
                exit(0)
        except ValueError as e:
            continue