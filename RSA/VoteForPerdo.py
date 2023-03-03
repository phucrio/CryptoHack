from fractions import gcd
from pwn import remote
import gmpy2
import json
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x)
    pass

ip, port  = "socket.cryptohack.org", 13375

FLAG = "aa"
ALICE_E = 3
ALICE_N = 22266616657574989868109324252160663470925207690694094953312891282341426880506924648525
181014287214350136557941201445475540830225059514652125310445352175047408966028497316806142156338
927162621004774769949534239479839334209147097793526879762417526445739552772039876568156469224491
682030314994880247983332964121759307658270083947005466578077153185206199759569902810832114058818
478518470715726064960617482910172035743003538122402440142861494899725720505181663738931151677884
218457824676140190841393217857683627886497104915390385283364971133316672332846071665082777884028
170668140862010444247560019193505999704028222347577

def vote(v):
    if local:
        verified_vote = long_to_bytes(pow(v, ALICE_E, ALICE_N))

        # remove padding
        v = verified_vote.split(b'\00')[-1]

        print("[-] DEBUG verified_vote:", verified_vote)
        print("[-] DEBUG v:", v)

        if v == b'VOTE FOR PEDRO':
            return {"flag": FLAG }
        else:
            return {"error": "You should have voted for Pedro" }
    else:
        re.sendline('{"option":"vote","vote":"%x"}' % v)
        return json.loads(re.readline())
    pass

local = False
if not local:
    re = remote(ip, port)
    re.readline()
    pass

# solution 1
# V = b'\x00VOTE FOR PEDRO'
# we need to find x where
# (x ** ALICE_E) mod (16 ** (len(V) * 2)) = int(V.hex(), 16)
# (x ** 3) mod (16 ** 30) = 1750572331061789800727934052618831
# using wolframealpha
# https://www.wolframalpha.com/input/?i=%28x+%5E+3%29+mod+%2816+%5E+30%29+%3D%3D+1750572331061789800727934052618831
# (x ^ 3) mod (16 ^ 30) == 1750572331061789800727934052618831
# 855520592299350692515886317752220783 + (16 ** 30) * n

# solution 2
V = b'\x00VOTE FOR PEDRO'
# we need to find x where
# (x ** ALICE_E) mod (16 ** (len(V) * 2)) == int(V.hex(), 16)
# int(V.hex(), 16) == pow(x, ALICE_E, 16 ** (len(V) * 2))
# int(V.hex(), 16) == pow(x, ALICE_E, 2 ** (len(V) * 2 * 4))
# x == pow(int(V.hex(), 16), d, 2 ** (len(V) * 2 * 4))
# where d * ALICE_E = 1 mod (2 ** (len(V) * 2 * 4))
c = int(V.hex(), 16)
n = 16 ** (len(V) * 2)

# since n can be expressed in the form 2 ** (len(V) * 2 * 4)
# phi(n) == n // 2
phi = n // 2

d = egcd(phi, ALICE_E)[2] % phi

v = pow(c, d, n)

assert pow(v, ALICE_E, ALICE_N) % n == c

j = vote(v)
print("[+] flag:", j['flag'])