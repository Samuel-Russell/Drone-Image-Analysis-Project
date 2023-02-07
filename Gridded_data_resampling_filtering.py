# Drone Data: Gridded data, including resampling and filtering

# Import Modules

import os
import rasterio as rio
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable 
from skimage import feature
from skimage import transform
from skimage import color
from scipy import ndimage
%matplotlib inline

os.lisdir('EXAMPLE_DATASET')

# Import Data
fn = 'FILE NAME' with rio.open(fn, 'r') as src:
    rgb = src.read() 
    rgb_meta = src.meta 
    src.close

#Subset
Subset_rgb_data = rgb[:, 1400:1600, 150:350] print(rgb_meta)
plt.figure(figsize=(8, 12)) plt.imshow(np.moveaxis(Subset_rgb_data, 0, -1));


# data is in data/Golm-UAV
fn = 'FILE_LOCATION'

with rio.open(fn, 'r') as src: 
    rgb = src.read() 
    rgb_meta = src.meta 
    src.close 

#Subset

Drone_Image_2 = rgb[:, 2350:2700, 1320:1700] 
print(rgb_meta) 
plt.figure(figsize=(8, 12))
plt.imshow(np.moveaxis(Drone_Image_2, 0, -1));

# TASK 2
# data is in data/Golm-UAV
fn = 'FILE_LOCATION'
with rio.open(fn, 'r') as src: 
    rgb = src.read() 
    rgb_meta = src.meta 
    src.close 
    
#Subset
Drone_airlidar = rgb[:, 1400:1600, 150:350] 
plt.figure(figsize=(8, 12))
plt.imshow(np.moveaxis(Drone_airlidar, 0, -1));

#Check data shape
Drone_airlidar.shape
