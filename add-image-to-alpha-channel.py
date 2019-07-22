#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys

if len(sys.argv) != 4:
    print("Bad arguments. Args: RGB image, alpha channel image and suffix.")
    exit()

rgb_file_name = sys.argv[1]
alpha_image_name = sys.argv[2]
alpha_type = sys.argv[3]
print("Image to modify: " + rgb_file_name)
print("Image to add as alpha channel: " + alpha_image_name)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

output_dir = "output"

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

rgb_image = Image.open(os.path.join(script_dir, rgb_file_name))
alpha_image = Image.open(os.path.join(script_dir, alpha_image_name))

alpha_image = alpha_image.convert("RGB")
r,g,b = alpha_image.split()

alpha = r.convert("L")

rgb_image.putalpha(alpha)

destination = output_dir + "/" + os.path.splitext(rgb_file_name)[0] + "_" + alpha_type + ".png"

rgb_image.save(os.path.join(script_dir, destination), "PNG")

print("Saved: " + destination)

exit()
