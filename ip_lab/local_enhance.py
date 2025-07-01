import matplotlib.pyplot as plt
import numpy as np


img = plt.imread('src/note_shadow2.png')[:,:,0]
M, N = img.shape
plt.imshow(img, cmap='grey')


def get_neighbourhood(img, i, j, r):
    i1, j1 = max(i-r, 0), max(j-r, 0)
    i2, j2 = min(i+r+1, M), min(j+r+1, N)
    return img[i1:i2, j1:j2]


def local_threshold(img, a, b, rad):
    M, N = img.shape
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
    
a, b, rad = 0.4, 0.9, 3
local_threshold(img, a, b, rad)