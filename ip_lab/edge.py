import matplotlib.pyplot as plt
import numpy as np

L = 256
img = plt.imread('src/temple4.png')[:,:,0]
M, N = img.shape


def convolve(img, kernel):
    m, n = kernel.shape
    assert m == n
    padded_img = np.pad(img, m//2)
    new_img = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            new_img[i, j] = np.tensordot(padded_img[i:i+m, j:j+m], kernel)
    return new_img

def threshold(img, T):
    return (img > T) * 1


laplacian = np.array([[1,1,1],[1,-8,1],[1,1,1]])
line = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
sobel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])


images = {
    'original': img,
    'point': threshold(convolve(img, laplacian), 1),
    'line_hor': threshold(convolve(img, line), 0.3),
    'line_ver': threshold(convolve(img, line.T), 0.3),
    'sobel_hor': threshold(convolve(img, sobel), 0.3),
    'sobel_ver': threshold(convolve(img, sobel.T), 0.3),
    'laplacian': threshold(convolve(img, laplacian), 0.3),
}


for name, image in images.items():
    plt.imsave(f'outputs/edge/{name}.png', image, cmap='grey')
    