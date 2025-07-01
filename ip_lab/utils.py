import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def saveimg2(img, name, fontsize=12):
    pilimg = Image.fromarray(img.astype('uint8')).convert('RGB')
    drawer = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("0xProtoNerdFont-Regular.ttf", fontsize)
    drawer.rectangle([(0,0), (fontsize*5.5, fontsize*2.5)], fill="#000") 
    drawer.text((0,0), 'Prasun\nAdhikari', font=font)
    pilimg.save(f'{name}.png')

def saveimg(img, name, fontsize=12):
    plt.imsave(f'{name}.png', img, cmap='grey')
    return
    pilimg = Image.fromarray(img).convert('RGB')
    drawer = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("0xProtoNerdFont-Regular.ttf", fontsize)
    drawer.rectangle([(0,0), (fontsize*5.5, fontsize*2.5)], fill="#000") 
    drawer.text((0,0), 'Prasun\nAdhikari', font=font)
    pilimg.save(f'{name}.png')

def watermark(folder, img_url):
    img = Image.open(f'{folder}/{img_url}')
    w, h = img.size
    fontsize = 14
    width = 600
    height = int(h/w*width)
    img = img.resize((width, height), 0)
    drawer = ImageDraw.Draw(img)
    font = ImageFont.truetype("0xProtoNerdFont-Regular.ttf", fontsize)
    drawer.rectangle([(0,0), (fontsize*5.5, fontsize*2.5)], fill="#000") 
    drawer.text((0,0), 'Prasun\n79010225', font=font)
    img.save(f'{folder}/water/{img_url}')

if __name__ == '__main__':
    watermark('.', 'lion_low.png')