from Crypto.Util.number import long_to_bytes
from sage.all import Matrix,GF
P = 2
N = 50
E = 31337

FLAG = b'crypto{??????????????????????????}'

def bin_to_bytes(s):
    all_bytes = [s[i:i+8] for i in range(0, len(s), 8)]
    return b''.join(long_to_bytes(int(byte, 2)) for byte in all_bytes)

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)

def find_GL_order():
    order = 1
    k = 0
    for k in range(N):
        order *= (P**N - P**k)
    
    assert order == GL(N, GF(P)).order()
    
    return order

C = load_matrix('flag.enc')

GLorder = find_GL_order()

D = pow(E, -1, GLorder)   

M = C^D

cols = M.columns()[:(len(FLAG)*8//50)+1]

bin_flag = ''.join([str(bit) for col in cols for bit in col])

print(bin_to_bytes(bin_flag))