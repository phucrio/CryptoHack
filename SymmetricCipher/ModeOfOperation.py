import requests

url = "https://aes.cryptohack.org/block_cipher_starter/"
r = requests.get(url + 'encrypt_flag/')
cipher_hex = r.json()['ciphertext']
print(cipher_hex)

r = requests.get(url+'decrypt/'+cipher_hex)
pt = r.json()['plaintext']
print(bytes.fromhex(pt))