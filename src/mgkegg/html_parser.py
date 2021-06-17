#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import re

class html:
    def __init__(self, url):
       self.url = url 
    def localize(self):
        mapname = os.path.basename(self.url).split('.')[0]
        with open(self.url) as inf:
            html_text = inf.read()
        with open(self.url, 'w') as outf:
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

    def cordinate(self):
        conf = []
        with open(self.url) as f:
            for line in f:
                    
                i = re.findall(r'<area id="\w+" shape="(\w+)" coords="(.+?)".+?title="(.+?)"', line)
                
                if len(i) > 0:
                    kegg_object = re.findall('(\w+) \(.+?\)[,]?', i[0][-1])
                    if len(kegg_object) > 0:
                        conf.append(i[0][:-1] + tuple(kegg_object))
        return conf
    
    
                           
                            
                                    