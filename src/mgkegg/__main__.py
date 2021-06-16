#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Qingyuan Zhang
# Date: 2021/06/15
# Version: 1.0.0
import argparse
from requests.sessions import should_bypass_proxies
from mgkegg.rest import *
from mgkegg.downloads import *

def main():
    parser = argparse.ArgumentParser(prog = "mgkegg", 
    description = 'KEGG color pathway object for metagenome')
    subparsers = parser.add_subparsers(dest='subcommand')


    parser_ls = subparsers.add_parser('ls', 
    help = 'list – obtain a list of entry identifiers and associated definition')
    parser_ls.add_argument('dbentries', metavar='dbentries', nargs='+', 
    help="""This operation can be used to obtain a list of all entries in each database.  \
        <database> = pathway | brite | module | ko | genome | <org> | vg | vp | ag | compound |
        glycan | reaction | rclass | enzyme | network | variant | disease |
        drug | dgroup | organism | <medicus> """)

    parser_find = subparsers.add_parser('find', 
    help = 'find – find entries with matching query keyword or other query data')
    parser_find.add_argument('dbentries', metavar='dbentries', nargs='+', 
    help="""This is a search operation.  \
        <database> = pathway | brite | module | ko | genome | <org> | vg | vp | ag | compound |
        glycan | reaction | rclass | enzyme | network | variant | disease |
        drug | dgroup | organism | <medicus> """)
        
    parser_info = subparsers.add_parser('info', 
    help='info – display database release information and linked db information')
    parser_info.add_argument('database', metavar='database', nargs='?',
    help="""This operation displays the database release information with statistics for the databases
    <database> = kegg | pathway | brite | module | ko | genome | genes | <org> | vg | vp |
    ag | ligand | compound | glycan | reaction | rclass | enzyme | network |
    variant | disease | drug | dgroup""")

    

    parser_get = subparsers.add_parser('get', 
    help = 'find – find entries with matching query keyword or other query data')
    parser_get.add_argument('dbentries', metavar='dbentries', nargs='+',
    help = """This operation retrieves given database entries in a flat file format or in other formats
    <database> = pathway | brite | module | ko | genome | <org> | vg | vp | ag | compound |
             glycan | reaction | rclass | enzyme | network | variant | disease |
             drug | dgroup | disease_ja | drug_ja | dgroup_ja | compound_ja

    <option> = aaseq | ntseq | mol | kcf | image | conf | kgml | json""")

    parser_download = subparsers.add_parser('download',
    help = 'download - download latest kegg reference maps with both png and html format')
    
    args = parser.parse_args()
    if args.subcommand == 'ls':
        display(['list'] + args.dbentries)
    if args.subcommand == 'find':
        display(['find'] + args.dbentries)
    if args.subcommand == 'info':
        display(['info'] + [args.database])
    if args.subcommand == 'get':
        display(['get'] + args.dbentries)
    if args.subcommand == 'download':
        download()

if __name__ == '__main__':
    main()