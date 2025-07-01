import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('src/scenenoise.png')[:,:,0]
M, N = img.shape


def nhood(img, i, j, m, n):
    i1, j1 = max(i-m, 0), max(j-m, 0)
    i2, j2 = min(i+n+1, M), min(j+n+1, N)
    return img[i1:i2, j1:j2]

def apply_filter(img, m, n, func, **kwargs):
    new_img = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            sxy = nhood(img, i, j, m, n)
            new_img[i, j] = func(sxy.flatten(), **kwargs)
    return new_img


def geo_mean(sxy):
    return np.pow(np.prod(sxy), 1/sxy.size)

def contra_harmonic(sxy, q):
    return np.sum(sxy**(q+1)) / np.sum(sxy**q)

def midpoint(sxy):
    return 1/2 * (np.min(sxy) + np.max(sxy))
    
def trimmed_mean(sxy, d):
    if d == 0:
        return np.mean(sxy)
    return np.mean(np.sort(sxy)[d//2:-d//2])


m, n = 3, 3

images = {
    'original': img,
    'arithmetic_mean': apply_filter(img, m, n, np.mean),
    'geometic_mean': apply_filter(img, m, n, geo_mean),
    'harmonic_mean': apply_filter(img, m, n, contra_harmonic, q=-1),
    'contra-harmonic_mean': apply_filter(img, m, n, contra_harmonic, q=2),
    'median': apply_filter(img, m, n, trimmed_mean, d=m*n-1),
    'min': apply_filter(img, m, n, np.min),
    'max': apply_filter(img, m, n, np.max),
    'midpoint': apply_filter(img, m, n, midpoint),
    'alpha-trimmed': apply_filter(img, m, n, trimmed_mean, d=m*n//2)
}

# m, n = 2, 2
for name, image in images.items():
    plt.imsave(f'outputs/stat/{name}.png', image, cmap='grey')

