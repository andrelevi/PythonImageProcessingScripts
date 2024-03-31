#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set image", required=True)
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument("-c", '--channels', help="Set channels to invert (RGBA)", required=True)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

args=parser.parse_args()

print("Directory: " + args.directory)
print("Image to modify: " + args.image_name)
print("Target channels: " + args.channels)

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

if "r" in args.channels.lower():
  r = invert(r)

if "g" in args.channels.lower():
  g = invert(g)

if "b" in args.channels.lower():
  b = invert(b)

if "a" in args.channels.lower():
  a = invert(a)

inverted_image = Image.merge(image.mode, (r, g, b, a))

destination = dir.strip('/') + "/" + os.path.splitext(args.image_name)[0] + "_inverted_" + args.channels + "." + args.image_type

inverted_image.save(destination, args.image_type)

print("Saved: " + destination)

exit()
