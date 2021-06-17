#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mgkegg.html_parser import *
from PIL import ImageColor, ImageDraw
import re

def get_gene(ls:str) -> list:
    """
    get gene and color from file
    """
    with open(ls) as f:
        return [line.strip() for line in f if line !='\n']  


def highlight_rect(coords:list, image:str, color:str):
    img = image
    for i in coords:
        if len(re.findall(r'\d+', i)) != 4:
            continue
        j = [int(x) for x in re.findall(r'\d+', i)]
        
        color1 = ImageColor.getcolor(color, 'RGBA')
        X, Y, RX, RY = j
        for x in range(X, RX):
            for y in range(Y, RY):
                if img.getpixel((x, y))[0] > 0:
                    ImageDraw.floodfill(img, xy=(x, y), value = color1)
    return img

def highlight_poly(coords:list, image:str, color:str):
    poly = []
    for i in coords:
        position = [int(x) for x in re.findall(r'\d+', i)]
        for x in range(1, len(position)):
            if x % 2 == 1:
                poly.append(tuple(position[x-1:x+1]))
        color1 = ImageColor.getcolor(color, 'RGBA')
        img = ImageDraw.ImageDraw(image)
        img.polygon(poly, color)
    return image
