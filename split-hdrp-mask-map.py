#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys

if len(sys.argv) != 2:
    print("Bad arguments. Args: Path to mask image.")
    exit()

mask_name = sys.argv[1]

print("Mask texture: " + mask_name)

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

output_dir = script_dir + "./"
print("Output dir: " + output_dir);

# Opening image.
maskMap = Image.open(os.path.join(script_dir, mask_name))
print(maskMap.format, maskMap.size, maskMap.mode)

name = os.path.splitext(mask_name)[0];
print("Name: " + name);

# Splitting channels
r,g,b,x = maskMap.split()

# Converting channels into maps.
metallness = r.convert("RGB")
metallness.save(os.path.join(output_dir, name + "_Metallic.png"), "PNG")

smoothness = x.convert("L")
smoothness.save(os.path.join(output_dir, name + "_Smoothness.png"), "PNG")

metallness.putalpha(smoothness)
metallness.save(os.path.join(output_dir, name + "_Metallic_Smoothness.png"), "PNG")

ao = g.convert("L")
ao.save(os.path.join(output_dir, name + "_AO.png"), "PNG")

detailMaskMap = b.convert("L")
detailMaskMap.save(os.path.join(output_dir, name + "_DetailMaskMap.png"), "PNG")
