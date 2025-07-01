import matplotlib.pyplot as plt
import numpy as np
from utils import saveimg2

oimg = plt.imread('lion.jpg')
N = min(oimg.shape[:2])
img = oimg[:N, :N, 0]


u, v = np.meshgrid(np.arange(N), np.arange(N))


def transform(img, N, direction=1):
    omega = np.exp(-2j * np.pi / N)
    # Generate DFT / iDFT matrix
    W = omega ** (direction * u * v)
    return W.dot(img).dot(W) / N**0.5


def apply_filter(img, filter):
    fxy = img * (-1)**(u+v)
    fuv = transform(fxy, N, 1)
    guv = fuv * filter
    gxy = transform(guv, N, -1)
    filtered_img = gxy * (-1)**(u+v)
    return np.real(filtered_img)



D0 = 5
duv = ((u-N/2)**2 + (v-N/2)**2)**0.5
n = 2
w = 10

# band reject filters
filters = {
    'ideal': abs(duv - D0) > w/2,
    'butterworth': 1 / (1 + (duv * w / (duv**2 - D0**2))**(2*n)),
    'gaussian': 1 - np.exp(-1/2 * ((duv**2 - D0**2) / (duv * w))**2)
}


plt.imsave('outputs/filters_band/original.png', img, cmap='grey')
for fname, brf in filters.items():
    brf_img = apply_filter(img, brf)
    bpf_img = apply_filter(img, 1 - brf)
    plt.imsave(f'outputs/filters_band/{fname}_reject.png', brf_img, cmap='grey')
    plt.imsave(f'outputs/filters_band/{fname}_pass.png', bpf_img, cmap='grey')