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


## Note:
## You can use the trimmed audio in memory instead of writing to disk
## by using the following code:
## import numpy as np
## trimmed_audio = audio.subclip(0, 15)
## sound_array = trimmed_audio.to_soundarray(tt=10, fps=16000)
## sound_bytes = sound_array.astype(np.int16).tobytes()
## song = await shazam.recognize(sound_bytes)
## However, I keep getting the error on the last line due to
## "SignatureError: FFmpeg not found or failed to convert audio"
## I think this is because we are running python from a venv and it can't
## locate the installed ffmpeg. Not sure if this is worth troubleshooting.


match filetype:
    case "mp3":
        print("mp3")
    case "mp4":
        print("mp4")
        audio = AudioFileClip(args.path)
        trimmed_audio = audio.subclip(0, 15)
        trimmed_audio.write_audiofile("trimmed.mp3")
        print("Trimmed audio saved as trimmed.mp3")
    case _:
        assert False, "Unknown file type"



async def main():
    shazam = Shazam()
    song = await shazam.recognize("trimmed.mp3")
    pprint(song)




loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("I do nothing yet...")
