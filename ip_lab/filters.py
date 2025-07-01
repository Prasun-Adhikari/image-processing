import matplotlib.pyplot as plt
import numpy as np

oimg = plt.imread('src/scene.png')
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

filters = {
    'ilpf': duv < D0,
    'blpf': 1 / (1 + (duv / D0)**(2*n)),
    'glpf': np.exp(-duv**2 / (2 * D0**2)),
    'ihpf': duv >= D0,
    'bhpf': 1 / (1 + (D0 / duv)**(2*n)),
    'ghpf': 1 - np.exp(-duv**2 / (2 * D0**2)),
    'lhpf': - 4 * np.pi**2 * duv**2
}


plt.imsave('outputs/filters/original.png', img, cmap='grey')
for lpfname, lpf in filters.items():
    lpf_img = apply_filter(img, lpf)
    plt.imsave(f'outputs/filters/{lpfname}.png', lpf_img, cmap='grey')
    