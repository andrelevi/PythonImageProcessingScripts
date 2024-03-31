#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set image", required=True)
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

_, image_extension = os.path.splitext(os.path.join(dir, args.image_name))
image = Image.open(os.path.join(dir, args.image_name)).convert('RGBA')

print(image.width)

r, g, b, a = image.split()

width = args.width if args.width != -1 else image.width
height = args.height if args.height != -1 else image.height

resized_image = image.resize((width, height))

destination = dir.strip('/') + "/" + os.path.splitext(args.image_name)[0] + "_resized" + "." + args.image_type

resized_image.save(destination, args.image_type)

print("Saved: " + destination)

exit()
