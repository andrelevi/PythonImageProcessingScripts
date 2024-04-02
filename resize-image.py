#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set input image", required=True)
parser.add_argument("-o", '--output_path', help="Set output path", required=False, default="")
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument("-w", '--width', help="Set width", required=False, default=-1, type=int)
parser.add_argument('--height', help="Set height", required=False, default=-1, type=int)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

args=parser.parse_args()

print("Directory: " + args.directory)
print("Image to modify: " + args.image_name)
print("Width: " + str(args.width))
print("Height: " + str(args.height))

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)
script_dir = os.path.dirname(__file__)

dir = script_dir if args.directory == "./" else args.directory

# Check if absolute path exists, if not try using relative path.
image_path = args.image_name if os.path.isfile(args.image_name) else os.path.join(dir, args.image_name)

_, image_extension = os.path.splitext(image_path)
image = Image.open(image_path).convert('RGBA')

r, g, b, a = image.split()

width = args.width if args.width != -1 else image.width
height = args.height if args.height != -1 else image.height

resized_image = image.resize((width, height))

file_name = os.path.splitext(os.path.basename(image_path))[0]

destination = dir.strip('/') + "/" + file_name + "_" + str(width) + "_" + str(height) + "." + args.image_type

if args.output_path != "":
  destination = args.output_path

resized_image.save(destination, args.image_type)

print("Saved: " + destination)

exit()
