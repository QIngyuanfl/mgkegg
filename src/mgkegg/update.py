#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mgkegg.downloads import *
from mgkegg.rest import *
import hashlib
import os




def update(database:str):
    """
    update kegg reference pathway database
    """

    try:
        with open (os.path.join(database, 'pathway.info'),'r') as f:
            former_text = f.read()
            print(former_text)
    except FileNotFoundError as err:
        raise SystemExit(err)
    f_md5 = hashlib.sha256(former_text)
    a_md5 = hashlib.sha256(get(['info', 'pathway']).encode())
    print(f_md5., a_md5)
    former_text.
    #download()