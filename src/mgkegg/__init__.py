import re
import os
from shutil import copyfile
from mgkegg.highlight import *
from mgkegg import html_parser
from PIL import Image
database = os.path.join(os.path.dirname(__file__), 'data')

def highlight(gls:list, color:str, database:str, outdir:str):
    kegg_object = get_gene(gls)
    for i in os.listdir(database):
        i = os.path.join(database, i)
        if re.search(r'map011\d+', i):
            copyfile(i, os.path.join(outdir, os.path.basename(i)))
            continue
        if 'html' not in i:
            continue
        conf = html(i).cordinate()
        cord_rect = []
        cord_poly = []
        for x in set(conf):
            for y in kegg_object:
                if y in ','.join(x[2:]):
                    if x[0] == 'rect':
                        cord_rect.append(x[1])
                    if x[0] == 'poly':
                        cord_poly.append(x[1])
                else:
                    continue
        if len(cord_rect) == 0 and len(cord_poly) == 0:
            continue
         
        img = Image.open(i.replace('html', 'png')).convert("RGB")
        
        if len(cord_rect) > 0:
            img = highlight_rect(cord_rect, img, color)
        if len(cord_poly) > 0:
            img = highlight_poly(cord_poly, img, color)
        copyfile(i, os.path.join(outdir, os.path.basename(i)))
        img.save(os.path.join(outdir, os.path.basename(i).replace('html', 'png')))    
