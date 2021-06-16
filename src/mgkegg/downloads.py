#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import float_repr_style
from mgkegg.rest import *
import asyncio
import aiohttp
import os
import re
import time

async def download_png(image:str, outdir:str):
    flag = True
    retry = 0
    url = f'http://rest.kegg.jp/get/{image}/image'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    while flag:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    with open(os.path.join(outdir, f'{image}.png'), 'wb') as pic:
                        while True:
                            chunk = await resp.content.read(64*1024)
                            if not chunk:
                                break
                            pic.write(chunk)
            flag = False
        except Exception:
            retry += 1
            time.sleep(1)
            flag = True
            print(f'retrying connect with {url} {retry} times')        

async def download_html(pathway:str, outdir:str):
    flag = True
    retry = 0
    url = f'https://www.kegg.jp/kegg-bin/show_pathway?{pathway}.html'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    while flag:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    with open(os.path.join(outdir, f'{pathway}.html'), 'w') as pic:
                        while True:
                            chunk = await resp.content.read(64*1024)
                            if not chunk:
                                break
                            pic.write(chunk)
            flag = False
        except Exception:
            retry += 1
            time.sleep(1)
            flag = True
            print(f'retrying connect with {url} {retry} times')

def download():
    """
Download png and html
    """
    datadir = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(datadir):
        os.makedirs(datadir)
    pathway_str = get(['list', 'pathway'])
    pathway_ls =  os.path.join(datadir, 'pathway.list')
    with open(pathway_ls, 'w') as f:
        f.write(pathway_str)
    pathway_list = []
    with open(pathway_ls) as f:
        for line in f:
            pathway_list += re.findall(r'path:(map\d{5})\t', line)
    flag = True
    tasks = []
    for i in range(len(pathway_list)):
        if flag: 
            loop = asyncio.new_event_loop()
            flag = False
        #tasks.append(loop.create_task(download_png(pathway_list[i], datadir)))
        tasks.append(loop.create_task(asyncio.sleep(1)))
        tasks.append(loop.create_task(download_html(pathway_list[i], datadir)))
        if i % 5 == 0:
            flag = True
            loop.run_until_complete(asyncio.gather(*tasks))
            loop.run_until_complete(asyncio.sleep(1))
            tasks = []
            loop.close()
    print(get(['info', 'pathway']), file=os.path.join(datadir, 'pathway.info'))                      

    

