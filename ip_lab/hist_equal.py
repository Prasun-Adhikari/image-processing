import matplotlib.pyplot as plt
import numpy as np

L = 256
img0 = plt.imread('src/temple3.png')
img = np.floor(img0[:,:,1] * (L-1)).astype(int)
M, N = img.shape


def get_histogram(img):
    histogram = np.zeros(L, dtype=int)
    for val in img.flatten():
        histogram[val] += 1
    return histogram



histogram = get_histogram(img0)
plt.bar(np.arange(0, L, dtype=int), histogram)
plt.text(220, 2000, 'Prasun\n79010225')
plt.savefig(f'outputs/hist/hist.png')
plt.show()


norm_histogram = histogram / (M * N)
plt.bar(np.arange(0, L, dtype=int), norm_histogram)
plt.text(220, 0.0165, 'Prasun\n79010225')
plt.savefig(f'outputs/hist/histnorm.png')
plt.show()


def cdf(norm_hist):
    s = np.zeros(L)
    for r in range(1, L):
        s[r] = s[r-1] + norm_hist[r]
    return np.floor(s * (L-1)).astype(int)


T = cdf(norm_histogram)
equalized_img = np.vectorize(lambda r: T[r])(img)


plt.imsave(f'outputs/hist/original.png', img, cmap='grey')
plt.imsave(f'outputs/hist/equalized.png', equalized_img, cmap='grey')