#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys
import PIL.ImageOps

if len(sys.argv) < 1:
    print("Bad arguments. Args: RGB image")
    exit()

file_name = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

print("Image to modify: " + file_name)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

output_dir = "./"

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

image = Image.open(os.path.join(script_dir, file_name)).convert('RGB')

resized_image = image.resize((width, height))

destination = output_dir + "/" + os.path.splitext(file_name)[0] + "_resized.png"

resized_image.save(destination, "PNG")

print("Saved: " + destination)

exit()
