#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mgkegg.rest import *
import aiohttp
import os

def download():
    
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "data")):
        os.makedirs(os.path.join(os.path.dirname(__file__), "data"))
    #print(os.path.realpath(sys.argv[0]))
    #pathway_str = get(['list', 'pathway']) 
    #print(pathway_str) 
    

