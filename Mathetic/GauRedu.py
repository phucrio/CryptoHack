import numpy as np
def dot(u,v): # napisałem własną funkcję mnożącą wektory, bo numpy dla dużych liczb nie działa
    return np.sum([ux*vx for ux, vx in zip(u, v)])

def gauss(v1, v2):
    while True:
        if dot(v1, v1) > dot(v2, v2): v1,v2=v2,v1  #(a) pierwiastek nie jest potrzebny bo więszka liczba ma większy pierwiastek
        m = dot(v1, v2) // dot(v1, v1)             #(b)
        if m == 0: return v1, v2                   #(c)
        v2 = [v2x-m*v1x for v1x,v2x in zip(v1,v2)] #(d)

u = [87502093, 123094980]
v = [846835985, 9834798552]

u, v = gauss(u, v)
print(u,v)
print(dot(u, v))