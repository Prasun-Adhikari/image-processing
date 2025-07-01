import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('region4.png')[:,:,0]
M, N = img.shape


def split_region(region):
    coords, bounds = region
    x1, y1, x2, y2 = bounds
    xm, ym = (x2 + x1)//2, (y2 + y1)//2
    subcoords = [set() for _ in range(4)]
    for x, y in coords:
        subcoords[2*(x >= xm) + (y >= ym)].add((x, y))
    return [(subcoords[0], (x1, y1, xm, ym)),
            (subcoords[1], (x1, ym, xm, y2)),
            (subcoords[2], (xm, y1, x2, ym)),
            (subcoords[3], (xm, ym, x2, y2))
           ]


def check_adjacency(region1, region2):
    for x1, y1 in region1[0]:
        for x2, y2 in region2[0]:
            if abs(x2-x1) + abs(y2-y1) <= 1:
                return True
    return False 


def merge_regions(region1, region2):
    x11, y11, x12, y12 = region1[1]
    x21, y21, x22, y22 = region2[1]
    return (region1[0]|region2[0], (min(x11,x21), min(y11,y21), max(x12,x22), max(y12,y22)))


def check_region(coords):
    mini, maxi = L, 0
    for coord in coords:
        mini = min(mini, img[coord])
        maxi = max(maxi, img[coord])
    return (maxi - mini) < 8/256


def find_and_merge():
    for region1 in regions:
        for region2 in regions:
            if region1 != region2 and check_adjacency(region1, region2):
                if check_region(region1[0]|region2[0]):
                    regions.remove(region1)
                    regions.remove(region2)
                    regions.insert(0, merge_regions(region1, region2))
                    return True
    return False



regions = [(set(), (0, 0, M, N))]
for i in range(M):
    for j in range(N):
        regions[0][0].add((i, j))



for _ in range(int(np.log2(max(M,N))) + 1):
    new_regions = []
    for region in regions:
        if not region[0]:
            continue
        if not check_region(region[0]):
            subregions = split_region(region)
            new_regions += subregions
        else:
            new_regions.append(region)
    regions = new_regions


for _ in range(len(regions)):
    if not find_and_merge():
        break


img_regions = np.zeros((M,N))
for i, region in enumerate(regions):
    for pos in region[0]:
        img_regions[pos] = i


plt.imsave('outputs/region/original_pix.png', img, cmap='grey')
plt.imsave('outputs/region/splitmerge.png', img_regions, cmap='grey')
