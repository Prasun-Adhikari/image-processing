import matplotlib.pyplot as plt
import numpy as np


L = 256
img0 = plt.imread('morpha.png')[:,:,3]
img = np.round(img0).astype(bool)
M, N = img.shape
plt.imshow(1-img, cmap='grey')



def nhood(img, i, j, r):
    return np.pad(img, r//2)[i:i+r, j:j+r]        


# structural element
r = 2
si = np.ones((r,r), dtype=bool)


def dilate(img):
    dilated = np.zeros((M, N), dtype=bool)
    for i in range(M):
        for j in range(N):
            dilated[i][j] = np.any(si & nhood(img, i, j, r))
    return dilated


def erode(img):
    eroded = np.zeros((M, N), dtype=bool)
    for i in range(M):
        for j in range(N):
            eroded[i][j] = np.all(~si | nhood(img, i, j, r))
    return eroded


eroded = erode(img)
dilated = dilate(img)
opened = dilate(eroded)
closed = erode(dilated)

plt.imsave('outputs/morph/original.png', 1-img, cmap='grey')
plt.imsave('outputs/morph/eroded.png', 1-eroded, cmap='grey')
plt.imsave('outputs/morph/dilated.png', 1-dilated, cmap='grey')
plt.imsave('outputs/morph/opened.png', 1-opened, cmap='grey')
plt.imsave('outputs/morph/closed.png', 1-closed, cmap='grey')
