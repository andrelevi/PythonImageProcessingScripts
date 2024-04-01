#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set image", required=True)
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument("-c", '--channel', help="Set channel to extract (RGBA)", required=True)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

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

#output_image = Image.new().convert('RGBA')

channels = (r, g, b, a)

if args.channel == "r":
  channels = (r, r, r, a)

if args.channel == "g":
  channels = (g, g, g, a)

if args.channel == "b":
  channels = (b, b, b, a)

output_image = Image.merge(image.mode, channels)

destination = dir.strip('/') + "/" + os.path.splitext(args.image_name)[0] + "_extracted_" + args.channel + "." + args.image_type

output_image.save(destination, args.image_type)

print("Saved: " + destination)

exit()
