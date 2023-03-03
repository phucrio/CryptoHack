import numpy as np
import sage
ar = np.array
v = ar([846835985, 9834798552],dtype='i8')
u = ar([87502093, 123094980],dtype='i8')
v1,v2 = u,v
if np.absolute(v2.all()) < np.absolute(v1.all()):
    print("swap")
    v1,v2 = v2,v1
m = int(v1.dot(v2)/v1.dot(v1))
v2 = v2 -m*v1
if np.absolute(v2.all()) < np.absolute(v1.all()):
    print("swap")
    v1,v2 = v2,v1
m = int(v1.dot(v2)/v1.dot(v1))
print(v1.dot(v2))
np.absolute
