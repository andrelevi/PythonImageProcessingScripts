#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-rgb", '--rgb_image_name', help="Set RGB image", required=True)
parser.add_argument("-alpha", '--alpha_image_name', help="Set Alpha image", required=True)
parser.add_argument("--suffix", help="Set suffix for output image", required=False, default="smoothness")
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument('--exponent_power', help="Exponential power of the alpha image", required=False, default=1)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

args=parser.parse_args()

print("Directory: " + args.directory)
print("RGB image: " + args.rgb_image_name)
print("Alpha image: " + args.alpha_image_name)
print("Exponent power: " + str(args.exponent_power))

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)
script_dir = os.path.dirname(__file__)

dir = script_dir if args.directory == "./" else args.directory

_, rgb_image_extension = os.path.splitext(os.path.join(dir, args.rgb_image_name))
rgb_image = Image.open(os.path.join(dir, args.rgb_image_name)).convert("RGB")
alpha_image = Image.open(os.path.join(dir, args.alpha_image_name)).convert("RGB")

r,g,b = alpha_image.split()

if rgb_image.size != alpha_image.size:
    print("ERROR: Images are different sizes")
    print("RGB Image Size: " + str(rgb_image.size[0]) + "," + str(rgb_image.size[1]))
    print("Alpha Image Size: " + str(alpha_image.size[0]) + "," + str(alpha_image.size[1]))
    exit()

alpha = r.convert("L")

def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))

if args.exponent_power != 1:
    for x in range(alpha.width):
        for y in range(alpha.height):
            pixel = alpha.getpixel((x,y))
            altered_pixel = pow(pixel, args.exponent_power)
            altered_pixel = clamp(altered_pixel, 0, 254) # 254 seems to be the max valid value
            altered_pixel = round(altered_pixel)
            alpha.putpixel((x, y), altered_pixel)

rgb_image.putalpha(alpha)

destination = dir.strip('/') + "/" + os.path.splitext(args.rgb_image_name)[0] + "_" + args.suffix + "." + args.image_type

rgb_image.save(destination)

print("Saved: " + destination)

exit()

