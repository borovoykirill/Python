#!/usr/bin/env python

import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-version", action="version", version='list-files v0.1',
                    help="Application version")
parser.add_argument("-path", required=True,
                    help="Output files only from the parent directory")
parser.add_argument("-rec", action="store_true", help="List files recursively")
parser.add_argument("-ext", nargs="?", const=1, default="", help="Filter by file extension")
parser.add_argument("-date", action="store_true", help="Order output by date")
args = parser.parse_args()


def get_date(m_time):
    d = datetime.utcfromtimestamp(m_time)
    date = d.strftime("%Y %m %d")
    return date


data_list = []

if args.ext:
    filter_ext = args.ext
else:
    filter_ext = ""


def file_list(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(filter_ext):
                if args.date:
                    info = entry.stat()
                    data_list.append(f"Date: {get_date(info.st_mtime)} | {entry.name}")
                else:
                    data_list.append(entry.name)
            elif entry.is_dir() and args.rec:
                file_list(entry.path)


file_list(args.path)
data_list.sort()
for i in data_list:
    print(i)
