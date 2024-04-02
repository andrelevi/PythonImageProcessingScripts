#!/usr/local/bin/python3

from PIL import Image
import argparse
from utils import get_path, get_dir, save_image

parser=argparse.ArgumentParser()

parser.add_argument("-rgb", '--rgb_image_name', help="Set RGB image", required=True)
parser.add_argument("-alpha", '--alpha_image_name', help="Set Alpha image", required=True)
parser.add_argument("-o", '--output_path', help="Set output path", required=False, default="")
parser.add_argument("--suffix", help="Set suffix for output image", required=False, default="smoothness")
parser.add_argument("-d", '--directory', help="Set directory. Defaults to CWD", required=False, default="./images/")
parser.add_argument('--exponent_power', help="Exponential power of the alpha image", required=False, default=1)
parser.add_argument('--image_type', help="Set image type", required=False, default="png")

args=parser.parse_args()

print("Directory: " + args.directory)
print("RGB image: " + args.rgb_image_name)
print("Alpha image: " + args.alpha_image_name)
print("Exponent power: " + str(args.exponent_power))

dir = get_dir(args.directory)

rgb_image_path, rgb_image_extension = get_path(args.rgb_image_name, dir)
alpha_image_path, alpha_image_extension = get_path(args.alpha_image_name, dir)

rgb_image = Image.open(rgb_image_path).convert("RGB")
alpha_image = Image.open(alpha_image_path).convert("RGB")

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

save_image(rgb_image, args.suffix, rgb_image_path, dir, args.image_type, args.output_path)

exit()

