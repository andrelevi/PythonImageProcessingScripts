#!/usr/local/bin/python3

from PIL import Image
import argparse
from utils import get_path, get_dir, save_image

parser=argparse.ArgumentParser()

parser.add_argument("-i", '--image_name', help="Set image", required=True)
parser.add_argument("-o", '--output_path', help="Set output path", required=False, default="")
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument("-c", '--channel', help="Set channel to extract (RGBA)", required=True)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

args=parser.parse_args()

print("Directory: " + args.directory)
print("Image to modify: " + args.image_name)
print("Target channel: " + args.channel)

dir = get_dir(args.directory)

image_path, image_extension = get_path(args.image_name, dir)

image = Image.open(image_path).convert('RGBA')

r, g, b, a = image.split()

channels = (r, g, b, a)

if args.channel == "r":
  channels = (r, r, r, a)

if args.channel == "g":
  channels = (g, g, g, a)

if args.channel == "b":
  channels = (b, b, b, a)

if args.channel == "a":
  channels = (a, a, a, a)

output_image = Image.merge(image.mode, channels)

suffix = "_extracted_" + args.channel

save_image(output_image, suffix, image_path, dir, args.image_type, args.output_path)

exit()
