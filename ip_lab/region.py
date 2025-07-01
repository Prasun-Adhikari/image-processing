import matplotlib.pyplot as plt
import numpy as np
from collections import deque

img = plt.imread('wall_low.png')[:,:,0]
M, N = img.shape

def traverse_bfs(start):
    region = {start}
    visited = {start}
    queue = deque({start})
    while queue:
        temp = queue.popleft()
        x, y = temp
        for dx, dy in [(0,-1), (0,1), (1,0), (-1,0)]:
            nx, ny = x+dx, y+dy
            node = nx, ny
            if 0 <= nx < M and 0 <= ny < N and node not in visited:
                if condition(node, start):
                    region.add(node)
                    queue.append(node)
                visited.add(node)
    return region


def condition(seed, coord):
    return abs(img[seed] - img[coord]) < 0.2


def region_grow():
    regions = []
    for seed in seeds:
        region = traverse_bfs(seed)
        regions.append(region)
    

    new_img = np.zeros_like(img)
    for i, region in enumerate(regions):
        for pos in region:
            new_img[pos] = i+1
    
    return new_img

# seeds obtained manually
seeds = {(115, 150), (120, 190), (100, 250), (200, 0)}
grown_img = region_grow()

plt.imsave('outputs/region/original.png', img, cmap='grey')
plt.imsave('outputs/region/grown.png', grown_img, cmap='grey')