#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import re
def html_localize(file_name):
    mapname = os.path.basename(file_name).split('.')[0]
    with open(file_name) as inf:
        html_text = inf.read()
    with open(file_name, 'w') as outf:
        for line in html_text.split('\n'):
            if 'kegg2.html' in line:
                line = '   <a href="https://www.kegg.jp/kegg/kegg2.html"><img align="middle" alt="KEGG" border="0" src="https://www.kegg.jp/Fig/bget/kegg3.gif" /></a>\n'
            if re.search('<img .+ usemap="#mapdata"', line):
                line = f'<img src="{mapname}.png" name="pathwayimage" name="pathwayimage" usemap="#mapdata" border="0" />'
            href = re.compile(r'"(\/\S+)"')
            if href.search(line):
                line = href.sub(r'https://www.kegg.jp\1', line)
            man = re.compile(r"'(\/\S+)'")
            if man.search(line):
                line = man.sub(r"'https://www.kegg.jp\1'", line)
            line += '\n'
            outf.write(line)
