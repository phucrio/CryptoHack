import requests
import json

def get_encrypted():
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    r = requests.get(url)
    enc = (json.loads(r.text))['encrypted']
    return enc

enc = get_encrypted()
tmp = bytes.fromhex(enc)

enc_bytes = [tmp[i:i+16] for i in range(0,len(tmp),16)]

png_header = ['89', '50', '4E', '47', '0D', '0A', '1A', '0A', '00', '00', '00', '0D', '49', '48', '44', '52']


key_stream = ([int(a, 16)^b for a,b in zip(png_header,enc_bytes[0])])

p = []
for i in range(len(enc_bytes)):
    p.append(bytes([a^b for a,b in zip(key_stream,enc_bytes[i])]))

pt = b''
for i in p:
    pt += i

with open("flag.png", 'wb') as f:
    f.write(pt)