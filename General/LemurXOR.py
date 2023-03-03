import numpy as np
from PIL import Image

img1 = Image.open('cryptohack/General/lemur.png')
img2 = Image.open('cryptohack/General/flag.png')

n1 = np.array(img1)*255
n2 = np.array(img2)*255

#our images have a mode of RGB which is assumed to be an 8-bit int
n_image = np.bitwise_xor(n1, n2).astype(np.uint8)
#Convert to PIL image and save
Image.fromarray(n_image).save('n.png')