import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('src/cube.png')[:,:,0]
M, N = img.shape


def replicate(img, f):
    f = 2
    new_img = np.zeros((M*f, N*f))
    for i in range(M):
        for j in range(N):
            new_img[i*f:(i+1)*f, j*f:(j+1)*f] = img[i, j]
            
    return new_img


# interpolation for 2x zoom
def interpolate(img):
    def get(img, i, j):
        try:
            return img[i, j]
        except IndexError:
            return 0
            
    new_img = np.zeros((M*2, N*2))

    # Zero interlace
    for i in range(M):
        for j in range(N):
            new_img[i*2, j*2] = img[i, j]

    # Interpolate Rows
    for i in range(M):
        for j in range(N):
            new_img[i*2, j*2+1] = (img[i, j] + get(img, i, j+1)) / 2
    
    # Interpolate Columns
    for i in range(M):
        for j in range(2*N):
            new_img[i*2+1, j] = (new_img[2*i, j] + get(new_img, 2*i+2, j)) / 2

    return new_img


replicated = replicate(img, 2)
interpolate = interpolate(img)

plt.imsave(f'outputs/zoom/original.png', img, cmap='grey')
plt.imsave(f'outputs/zoom/replicated.png', replicated, cmap='grey')
plt.imsave(f'outputs/zoom/interpolated.png', interpolate, cmap='grey')

