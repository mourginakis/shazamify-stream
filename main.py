#!/usr/bin/env python3

import os
import argparse

import shazamio

## Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to the .mp4 or .mp3 file")
args = parser.parse_args()

## Diagnostics
assert os.path.exists(args.path), "File does not exist!"
filetype = args.path.split('.')[-1]
print(f"Working with file: {args.path}\n"
      f"File type: .{filetype}\n")



print("I do nothing yet...")
