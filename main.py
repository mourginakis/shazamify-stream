#!/usr/bin/env python3

## Imports
import os
import argparse
import asyncio
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from pprint import pprint


from shazamio import Shazam

## Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to the .mp4 or .mp3 file")
args = parser.parse_args()

## Diagnostics
assert os.path.exists(args.path), "File does not exist!"
filetype = args.path.split('.')[-1]
print(f"Working with file: {args.path}\n"
      f"File type: .{filetype}\n")


match filetype:
    case "mp3":
        print("mp3")
    case "mp4":
        print("mp4")
        audio = AudioFileClip(args.path)
        trimmed_audio = audio.subclip(0, 15)
        # TODO: Store this in memory instead of writing to disk
        trimmed_audio.write_audiofile("trimmed.mp3")
        print("Trimmed audio saved as trimmed.mp3")
    case _:
        assert False, "Unknown file type"



async def main():
    shazam = Shazam()
    # TODO: Use the trimmed audio in memory instead of reading from disk
    song = await shazam.recognize("trimmed.mp3")
    pprint(song)




loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("I do nothing yet...")
