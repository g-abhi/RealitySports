# rename images in folder to sequential order, from filename sorted Alpha

import os
import tqdm as tqdm

base_dir = "../datasets/odell_football_demo/images"
counter = 1
for file in os.listdir(base_dir):
    os.rename(f'{base_dir}{file}', f'{base_dir}obj{counter:03}.jpg')
    counter += 1

# cd {directory with imgs}
# python {path to colmap2nerf.py} --colmap_matcher exhaustive --run_colmap --aabb_scale 16 --overwrite