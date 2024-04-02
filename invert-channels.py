#!/usr/local/bin/python3

from PIL import Image
import argparse
from utils import get_path, get_dir, save_image

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set image", required=True)
parser.add_argument("-o", '--output_path', help="Set output path", required=False, default="")
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument("-c", '--channels', help="Set channels to invert (RGBA)", required=True)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

args=parser.parse_args()

print("Directory: " + args.directory)
print("Image to modify: " + args.image_name)
print("Target channels: " + args.channels)

dir = get_dir(args.directory)

image_path, image_extension = get_path(args.image_name, dir)

image = Image.open(image_path).convert('RGBA')

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

output_image = Image.merge(image.mode, (r, g, b, a))

suffix = "_inverted_" + args.channels

save_image(output_image, suffix, image_path, dir, args.image_type, args.output_path)

exit()
