#!/usr/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys

if len(sys.argv) != 4:
    print("Bad arguments. Args: RGB values, alpha channel image and suffix.")
    exit()

rgb_color_value = sys.argv[1]
alpha_channel_image = sys.argv[2]
suffix = sys.argv[3]
print("image to add as alpha channel: " + alpha_channel_image)
print("RBG color value: " + rgb_color_value)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

output_dir = "./"

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

alpha_image = Image.open(os.path.join(script_dir, alpha_channel_image))
rgb_image = Image.new('RGB', (alpha_image.width, alpha_image.height), rgb_color_value)

r,g,b = alpha_image.split()

alpha = r.convert("L")

rgb_image.putalpha(alpha)

destination = output_dir + "/" + os.path.splitext(alpha_channel_image)[0] + "_" + suffix + ".png"

rgb_image.save(os.path.join(script_dir, destination), "PNG")

print("Saved: " + destination)

exit()
