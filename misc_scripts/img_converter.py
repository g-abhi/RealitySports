# AP converter
# we need to convert .webp to .jpg
# and .png to .jpg

import os
from PIL import Image
from tqdm import tqdm

base_dir = "../datasets/odell_football_demo/images/"
files_webp_png = [x for x in os.listdir(base_dir) if ".webp" in x or ".png" in x]
# files_png = [x for x in os.listdir("../datasets/odell_football_demo/") if ".png" in x] 
# https://medium.com/@ajeet214/image-type-conversion-jpg-png-jpg-webp-png-webp-with-python-7d5df09394c9

for file in tqdm(files_webp_png):
    # convert each webp to jpg
    if ".webp" in file:
        filename = file.split(".webp")[0]
    else:
        filename = file.split(".png")[0]
        print(filename)
    im = Image.open(f'{base_dir}{file}').convert("RGB")
    im.save(f'{base_dir}{filename}.jpg', "jpeg")