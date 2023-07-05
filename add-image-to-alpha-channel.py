#!/usr/local/bin/python3

from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog
import os
import sys

def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))

if len(sys.argv) < 4:
    print("Bad arguments. Args: RGB image, alpha channel image, suffix, exponent power.")
    exit()

rgb_file_name = sys.argv[1]
alpha_image_name = sys.argv[2]
alpha_type = sys.argv[3]

exponent_power = 1

if len(sys.argv) >= 5: 
    exponent_power = float(sys.argv[4])

print("Image to modify: " + rgb_file_name)
print("Image to add as alpha channel: " + alpha_image_name)
print("Exponent power: " + str(exponent_power))

root = Tk()
root.withdraw()
root.call('wm','attributes','.','-topmost', True)

output_dir = "./"

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

rgb_image = Image.open(os.path.join(script_dir, rgb_file_name))
alpha_image = Image.open(os.path.join(script_dir, alpha_image_name))

alpha_image = alpha_image.convert("RGB")
r,g,b = alpha_image.split()

alpha = r.convert("L")

if exponent_power != 1:
    for x in range(alpha.width):
        for y in range(alpha.height):
            pixel = alpha.getpixel((x,y))
            altered_pixel = pow(pixel, exponent_power)
            altered_pixel = clamp(altered_pixel, 0, 254) # 254 seems to be the max valid value
            altered_pixel = round(altered_pixel)
            alpha.putpixel((x, y), altered_pixel)

rgb_image.putalpha(alpha)

destination = output_dir + "/" + os.path.splitext(rgb_file_name)[0] + "_" + alpha_type + ".png"

rgb_image.save(os.path.join(script_dir, destination), "PNG")

print("Saved: " + destination)

exit()

