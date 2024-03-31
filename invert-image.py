#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set image", required=True)
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./")
parser.add_argument("-c", '--channel', help="Set channel type to invert: 'rgb' or 'a'", required=True)

args=parser.parse_args()

print("Directory: " + args.directory)
print("Image to modify: " + args.image_name)
print("Target channel: " + args.channel)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

script_dir = os.path.dirname(__file__)

dir = script_dir if args.directory == "./" else args.directory

_, image_extension = os.path.splitext(os.path.join(dir, args.image_name))
image = Image.open(os.path.join(dir, args.image_name)).convert('RGBA')

r, g, b, a = image.split()

def invert(image):
    return image.point(lambda p: 255 - p)

if args.channel == "rgb":
  r, g, b = map(invert, (r, g, b))

if args.channel == "a":
  a = invert(a)

inverted_image = Image.merge(image.mode, (r, g, b, a))

destination = dir.strip('/') + "/" + os.path.splitext(args.image_name)[0] + "_inverted_" + args.channel + image_extension

inverted_image.save(destination)

print("Saved: " + destination)

exit()
