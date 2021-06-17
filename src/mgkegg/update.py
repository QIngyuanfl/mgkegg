#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mgkegg.downloads import *
from mgkegg.rest import *
import os
import re



def update(database:str):
    """
    update kegg reference pathway database
    """

    try:
        with open (os.path.join(database, 'pathway.info'),'r') as f:
            former_text = f.read()
    except FileNotFoundError as err:
        raise SystemExit(err)

    current_version = re.findall(f'Release (.+?)/', former_text)[0]
    former_version = re.findall(f'Release (.+?)/', get(['info', 'pathway']))[0]
    if current_version != former_version:
        download()
    else:
        print('You already have the latest version of kegg reference pathway')