#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys

if len(sys.argv) != 4:
    print("Bad arguments. Args: RGB image, alpha channel image, and target RGBA channel.")
    exit()

original_file_name = sys.argv[1]
channel_image_name = sys.argv[2]
target_channel = sys.argv[3]
print("Image to modify: " + original_file_name)
print("Image to add as channel: " + channel_image_name)
print("Target channel: " + target_channel)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

output_dir = "./"

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

original_image = Image.open(os.path.join(script_dir, original_file_name))
channel_image = Image.open(os.path.join(script_dir, channel_image_name))

orig_r,orig_g,orig_b,orig_a = original_image.split()
r,g,b = channel_image.split()

alpha = r.convert("L")

if target_channel == "r":
    original_image = Image.merge("RGBA", [r, orig_g, orig_b, orig_a])
elif target_channel == "g":
    original_image = Image.merge("RGBA", [orig_r, g, orig_b, orig_a])
elif target_channel == "b":
    original_image = Image.merge("RGBA", [orig_r, orig_g, b, orig_a])

#original_image.putalpha(alpha)

destination = output_dir + "/" + os.path.splitext(original_file_name)[0] + "_packed.png"

original_image.save(os.path.join(script_dir, destination), "PNG")

print("Saved: " + destination)

exit()
