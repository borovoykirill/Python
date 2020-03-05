#!/usr/bin/env python

import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-version", action="version", version='dir-stats v0.1',
                    help="Application version")
parser.add_argument("-dir", nargs="?", const=1, default=".",
                    help="Output files only from the parent directory")
parser.add_argument("-recurs", nargs=1, help="List files recursively")
parser.add_argument("-ext", nargs=2, help="Filter by file extension")
parser.add_argument("-fname", nargs=1, help="Order output by filename")
parser.add_argument("-fdate", nargs=1, help="Order output by date")
args = parser.parse_args()


# "Output files only from the parent directory"
def dir_files(path):
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)


if args.dir:
    dir_files(args.dir[0])


# "List files recursively"
def files_recursive(path):
    if args.recurs:
        for dirpath, dirs, files in os.walk(path):
            path = dirpath.split('/')
            print('|', (len(path)) * '---', '[', os.path.basename(dirpath), ']')
        for f in files:
            print('|', len(path) * '---', f)


if args.recurs:
    files_recursive(args.recurs[0])


# "Filter by file extension"
def files_extension(path):
    for file in os.listdir(path):
        if file.endswith('.' + args.ext[1]):
            print(os.path.join(path, file))


if args.ext:
    files_extension(args.ext[0])

# "Order by name"
namelist = []


def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                namelist.append(str(entry.name))
                namelist.sort()
            elif entry.is_dir():
                list_files(entry.path)


if args.fname:
    list_files(args.fname[0])
    print("\n".join(str(x) for x in namelist))


# "Order output by date"
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                info = entry.stat()
                print(f'{convert_date(info.st_mtime)}\t {entry.name} ')
            elif entry.is_dir():
                list_files(entry.path)


if args.fdate:
    list_files(args.fdate[0])
