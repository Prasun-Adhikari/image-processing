import matplotlib.pyplot as plt
import numpy as np

img1 = plt.imread('src/coin.png')[:,:,0]
img2 = plt.imread('src/note_shadow2.png')[:,:,0]
M, N = img2.shape

def global_threshold(img):
    T = 0.5
    dT = 0.001
    while True:
        m1 = np.sum((img > T) * img) / np.sum(img > T)
        m2 = np.sum((img < T) * img) / np.sum(img < T) 
        newT = (m1 + m2) / 2
        if abs(T - newT) < dT:
            break
        T = newT
    return (img>T)*1


def get_neighbourhood(img, i, j, r):
    i1, j1 = max(i-r, 0), max(j-r, 0)
    i2, j2 = min(i+r+1, M), min(j+r+1, N)
    return img[i1:i2, j1:j2]


def local_threshold(img, a, b, rad):
    mg = np.mean(img)
    sg = np.std(img)
    new_img = np.zeros((M, N))
    for x in range(M):
        for y in range(N):
            neigh = get_neighbourhood(img, x, y, rad)
            txy = a * np.std(neigh) + b * np.mean(neigh)
            # print(txy, img[x, y])
            if img[x, y] > txy:
                new_img[x, y] = 1
            else:
                new_img[x, y] = 0
    return new_img

global_img = global_threshold(img1)
local_img = local_threshold(img2, a=0.4, b=0.9, rad=3)

plt.imsave('outputs/thresh/original1.png', img1, cmap='grey')
plt.imsave('outputs/thresh/original2.png', img2, cmap='grey')
plt.imsave('outputs/thresh/global.png', global_img, cmap='grey')
plt.imsave('outputs/thresh/local.png', local_img, cmap='grey')

