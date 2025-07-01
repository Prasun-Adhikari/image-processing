from utils import watermark
import os

def watermark_folder(folder):
    folder = f'outputs/{folder}'
    os.makedirs(f'{folder}/water', exist_ok=True)
    for file in os.listdir(folder):
        try:
            watermark(folder, file)
        except IsADirectoryError:
            pass

# folders = ['point', 'hist', 'zoom', 'filters', 'stat', 'filters_band', 'edge', 'thresh', 'region']
# for folder in folders:
#     watermark_folder(folder)

watermark_folder('zoom')