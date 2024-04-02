#!/usr/local/bin/python3

from PIL import Image
from tkinter import Tk
import os
import argparse

def save_image(image, suffix, path, dir, image_type, output_path):
  file_name = os.path.splitext(os.path.basename(path))[0]

  destination = dir.strip('/') + "/" + file_name + "_" + suffix + "." + image_type

  if output_path != "":
    destination = output_path

  image.save(destination, image_type)
  
  print("Saved: " + destination)

def get_dir(directory):
  root = Tk()
  root.withdraw()
  root.call('wm','attributes','.','-topmost', True)
  script_dir = os.path.dirname(__file__)

  return script_dir if directory == "./" else directory


def get_path(input_path, directory):
  # Check if absolute path exists, if not try using relative path.
  return (input_path if os.path.isfile(input_path) else os.path.join(directory, input_path), os.path.splitext(input_path))