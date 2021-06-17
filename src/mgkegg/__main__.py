#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Qingyuan Zhang
# Date: 2021/06/15
# Version: 1.0.0
import argparse
from requests.sessions import should_bypass_proxies
from mgkegg import downloads, highlight
from mgkegg.rest import *
from mgkegg.downloads import *
from mgkegg.update import *
from mgkegg.html_parser import *
import mgkegg

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
    help = 'download - download the latest kegg reference maps with both png and html format')

    parser_update = subparsers.add_parser('update', 
    help = 'update - update to the latest kegg reference maps database')
    
    parser_highlight = subparsers.add_parser('highlight', 
    help = 'highlight - highlight the given IDs of kegg components')

    parser_highlight.add_argument('--glist', metavar='genelist', 
    help = 'a file include gene list of kegg objects')

    parser_highlight.add_argument('--outdir', '-o', 
    help='outputdir for result')

    parser_highlight.add_argument('--color', help='background highlight color')

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
        print('start downloading...')
        download()
    if args.subcommand == 'update':
        print('start updating...')
        update(downloads.datadir)
    if args.subcommand == 'highlight':
        color = args.color
        gls = args.glist
        outdir = args.outdir
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        highlight(gls, color, mgkegg.database, outdir)
    if not args.subcommand:
        parser.print_help()
if __name__ == '__main__':
    
    main()
