#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys

if len(sys.argv) < 1:
    print("Bad arguments. Args: RGB image")
    exit()

file_name = sys.argv[1]

print("Image to modify: " + file_name)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

output_dir = "./"

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

image = Image.open(os.path.join(script_dir, file_name)).convert('RGBA')

alpha = image.split()[-1]

# Create a new image with an opaque black background
bg = Image.new("RGBA", image.size, (0,0,0,255))

# Copy the alpha channel to the new image using itself as the mask
bg.paste(alpha, mask=alpha)

# Since the bg image started as RGBA, we can save some space by converting it
# to grayscale ('L') Optionally, we can convert the image to be indexed which
# saves some more space ('P') In my experience, converting directly to 'P'
# produces both the Gray channel and an Alpha channel when viewed in GIMP,
# althogh the file sizes is about the same

destination = output_dir + "/" + os.path.splitext(file_name)[0] + "_alpha.png"
bg.convert('L').convert('P', palette=Image.ADAPTIVE, colors=8).save(os.path.join(script_dir, destination), "PNG", optimize=True)

print("Saved: " + destination)

exit()
