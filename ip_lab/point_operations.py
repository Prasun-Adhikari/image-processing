import numpy as np
import matplotlib.pyplot as plt

L = 256
img0 = plt.imread('src/sceneryc.png')[:,:,0]
img = np.floor(img0 * (L-1)).astype(int)
M, N = img.shape


def tranform_save(img, func):
    new_img = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            new_img[i,j] = func(int(img[i,j]))

    plt.imsave(f'outputs/point/{func.__name__}.png', new_img, cmap='grey')
    

plt.imsave(f'outputs/point/original.png', img, cmap='grey')

# negative
def negative(r):
    return (L-1) - r
tranform_save(img, negative)


# contrast stretch
r1, r2 = 60, 100
s1, s2 = 20, 120
a, b, c = s1/r1, (s2-s1)/(r2-r1), (L-1-s2)/(L-1-r2)
def contrast_stretch(r):
    if r < r1:
        return a * r
    elif r < r2:
        return b * (r-r1) + s1
    else:
        return c * (r-r2) + s2
tranform_save(img, contrast_stretch)


# log
c = L/np.log(1+L)
def log(r):
    return c * np.log(r+1)
tranform_save(img, log)


# Power law
gamma = 1.5
c = L**(1-gamma)
def power(r):
    return c * r**gamma
tranform_save(img, power)


# Bit plane
def bitplane(r):
    r = int(r)
    return int(r%(2**(b+1)) >= 2**b) * (L-1)
    
for b in range(8):
    tranform_save(img, bitplane)


# Cliping
r1, r2 = 80, 120
def clipping(r):
    if r1 <= r <= r2:
        return r
    else:
        return 0
tranform_save(img, clipping)


# Thresholding
t = 120
def thresholding(r):
    if r < t:
        return 0
    else:
        return L-1
tranform_save(img, thresholding)


# Inetensity level slicing
r1, r2 = 20, 80
def intensity_slicing(r):
    if r1 <= r <= r2:
        return L-1
    else:
        return r
tranform_save(img, intensity_slicing)

