import numpy as np
# from utils import saveimg
# from PIL import Image
import matplotlib.pyplot as plt

L = 256
# img = plt.imread('lion.jpg')[:,:,0]
img0 = plt.imread('src/sceneryc.png')[:,:,0]
img = np.floor(img0 * (L-1)).astype(int)
M, N = img.shape


def tranform_save(img, func, name):
    new_img = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            new_img[i,j] = func(int(img[i,j]))

    plt.imsave(f'outputs/point/{name}.png', new_img, cmap='grey')

# Bit plane
def bitplane(r):
    r = int(r)
    return int(r%(2**(b+1)) >= 2**b) * (L-1)
    
for b in range(8):
    tranform_save(img, bitplane, f'bitplane{b}')