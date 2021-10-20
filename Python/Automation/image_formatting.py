#!/usr/bin/env python3

"""
GOAL:
Given a directory of images the following changes should be applied to all of the images:
1. Rotated 90 deg clockwise.
2. Resized to (128x128)
3. Saved in .jpeg format

NOTE: The script should be IN the same folder with the images to be formatted

"""

from PIL import Image
from glob import glob
import os

# Iterate through each image in the folder
for img in glob('ic_*'): # ignore the images/.DS_Store file
    image = Image.open(img).convert('RGB')
    
    path, filename = os.path.split(img)
    filename = os.path.splitext(filename)[0] # get filename without extension
    image.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))

print('Done')