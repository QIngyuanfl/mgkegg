#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
rest_url = "http://rest.kegg.jp/"
def display(args):
    """
    request from kegg rest api
    """
    
    url = rest_url + '/'.join(args)
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    print(r.text)

def get(args):
    """
    get data from kegg rest api
    """
    url = rest_url + '/'.join(args)
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return r.text     