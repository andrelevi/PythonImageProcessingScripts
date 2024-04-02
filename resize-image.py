#!/usr/local/bin/python3

from PIL import Image
import argparse
from utils import get_path, get_dir, save_image

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

dir = get_dir(args.directory)

image_path, image_extension = get_path(args.image_name, dir)

image = Image.open(image_path).convert('RGBA')

r, g, b, a = image.split()

width = args.width if args.width != -1 else image.width
height = args.height if args.height != -1 else image.height

resized_image = image.resize((width, height))
suffix = str(width) + "_" + str(height)

save_image(resized_image, suffix, image_path, dir, args.image_type, args.output_path)

exit()