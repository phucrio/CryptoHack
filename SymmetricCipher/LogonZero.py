from pwn import *
import json

t = (b"\x00" * 28).hex()
data = {"option": "reset_password", "token": t}
r = connect('socket.cryptohack.org' ,13399)
r.recvline()
json_data = json.dumps(data).encode()

while 1:
    r.sendline(json_data)
    r.recvline()
    p = {"option": "authenticate", "password": ""}
    json_password = json.dumps(p).encode()
    r.sendline(json_password)
    out = (r.recvline()).decode()
    if "crypto" in out:
        print(out)
        break
    reset = {"option": "reset_connection"}
    json_reset = json.dumps(reset).encode()
    r.sendline(json_reset)
    r.recvline()