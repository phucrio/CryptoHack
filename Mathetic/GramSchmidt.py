import numpy as np

def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum([np.dot(v, b) / np.dot(b, b) * b for b in basis], axis=0)
        if (np.abs(np.linalg.norm(w)) > 1e-10):
            basis.append(w / np.linalg.norm(w))
    return np.array(basis)

v1 = np.array([4, 1, 3, -1])
v2 = np.array([2, 1, -3, 4])
v3 = np.array([1, 0, -2, 7])
v4 = np.array([6, 2, 9, -5])

vectors = np.array([v1, v2, v3, v4])
u = vectors[0]
for vi in vectors[1:]:
    mi = [np.dot(vi,uj)/np.dot(uj,uj) for uj in u]
    u += [vi - sum([mij*uj for mij,uj in zip(mi,u)])]
#orthonormal_basis = gram_schmidt(vectors)

#print(orthonormal_basis)
print(round(u[3][1],5))