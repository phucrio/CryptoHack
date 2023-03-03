import requests

r = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/').json() 
ciphertext = r['ciphertext']
iv = ciphertext[:32] 
ciphertext = ciphertext[32:]
r = requests.get('http://aes.cryptohack.org/symmetry/encrypt/'+ciphertext+'/'+iv+'/').json() 
plaintext = r['ciphertext'] 
plaintext = bytes.fromhex(plaintext) 
print(plaintext)