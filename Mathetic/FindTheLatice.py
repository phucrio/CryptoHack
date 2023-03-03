from Crypto.Util.number import inverse
import numpy as np
def decrypt(q, h, f, g, e):
    a = (f * e) % q
    m = (a * inverse(f, g)) % g
    return m

def dot(u,v): # napisałem własną funkcję mnożącą wektory, bo numpy dla dużych liczb nie działa
    return np.sum([ux*vx for ux, vx in zip(u, v)])

def gauss(v1, v2):
    while True:
        if dot(v1, v1) > dot(v2, v2): v1,v2=v2,v1  #(a) pierwiastek nie jest potrzebny bo więszka liczba ma większy pierwiastek
        m = dot(v1, v2) // dot(v1, v1)             #(b)
        if m == 0: return v1, v2                   #(c)
        v2 = [v2x-m*v1x for v1x,v2x in zip(v1,v2)] #(d)


q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523
u = [1, h]
v = [0, q]

u, v = gauss(u, v)

f = u[0]
g = u[1]
print(f,g)
m = decrypt(q,h,f,g,e)
print(bytes.fromhex(hex(m)[2:]).decode())