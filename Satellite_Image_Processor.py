#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:15:55 2025

@author: manasi
"""
import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('satellite_sample.jpg')  # Read the image file

# checking transparancy
if image.shape[2] == 4:
    image = image[..., :3]  

# convert to grayscale + averaging RGB values
gray_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

# create figure n axis
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# display grayscale image
axes[0].imshow(gray_image, cmap='gray')
axes[0].axis('off')  # Hide the axes
axes[0].set_title('Grayscale Image', fontsize=18, fontweight='bold', color='teal')

# colorbar
cbar = axes[0].figure.colorbar(axes[0].imshow(gray_image, cmap='gray'), ax=axes[0], orientation='vertical')
cbar.set_label('Pixel Intensity', fontsize=14)

# create n display hist
axes[1].hist(gray_image.ravel(), bins=256, color='gray', alpha=0.7)
axes[1].set_title('Histogram of Grayscale Image', fontsize=18, fontweight='bold', color='purple')
axes[1].set_xlabel('Pixel Intensity', fontsize=14)
axes[1].set_ylabel('Frequency', fontsize=14)
axes[1].grid(True, linestyle='--', alpha=0.6)

# add annotation to hist
axes[1].text(200, 5000, 'Peak Intensity', horizontalalignment='center', fontsize=12, color='black', style='italic')

# add title for figure
fig.suptitle('Image Processing with Matplotlib', fontsize=20, fontweight='bold', color='darkblue')

# adjust layout to prevent overlaping
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# how plots
plt.show()
