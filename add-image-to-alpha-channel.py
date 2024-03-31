#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import argparse, sys

def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))

parser=argparse.ArgumentParser()

parser.add_argument("-rgb", '--rgb_image_name', help="Set RGB image", required=True)
parser.add_argument("-alpha", '--alpha_image_name', help="Set Alpha image", required=True)
parser.add_argument("-suffix", help="Set suffix for output image", required=False, default="smoothness")
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./")
parser.add_argument("-e", '--exponent_power', help="Exponential power of the alpha image", required=False, default=1)

args=parser.parse_args()

print("Directory: " + args.directory)
print("RGB image: " + args.rgb_image_name)
print("Alpha image: " + args.alpha_image_name)
print("Exponent power: " + str(args.exponent_power))

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

rgb_image = Image.open(os.path.join(script_dir, args.rgb_image_name))
alpha_image = Image.open(os.path.join(script_dir, args.alpha_image_name))

alpha_image = alpha_image.convert("RGB")
r,g,b = alpha_image.split()

if rgb_image.size != alpha_image.size:
    print("ERROR: Images are different sizes")
    print("RGB Image Size: " + str(rgb_image.size[0]) + "," + str(rgb_image.size[1]))
    print("Alpha Image Size: " + str(alpha_image.size[0]) + "," + str(alpha_image.size[1]))
    exit()

alpha = r.convert("L")

if args.exponent_power != 1:
    for x in range(alpha.width):
        for y in range(alpha.height):
            pixel = alpha.getpixel((x,y))
            altered_pixel = pow(pixel, args.exponent_power)
            altered_pixel = clamp(altered_pixel, 0, 254) # 254 seems to be the max valid value
            altered_pixel = round(altered_pixel)
            alpha.putpixel((x, y), altered_pixel)

rgb_image.putalpha(alpha)

directory = args.directory.strip('/')
destination = directory + "/" + os.path.splitext(args.rgb_image_name)[0] + "_" + args.suffix + ".png"

rgb_image.save(os.path.join(script_dir, destination), "PNG")

print("Saved: " + destination)

exit()

