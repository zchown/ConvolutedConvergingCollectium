# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import tensorflow as tf
import os
import time
import datetime

from matplotlib import pyplot as plt
from IPython import display
import PIL
import numpy as np

# %%

def load(image_file):
    input_image = tf.io.read_file("dataset/skeletons/" + image_file)
    real_image = tf.io.read_file("dataset/animal/" + image_file)
    if image_file.endswith(".jpg"):
        input_image = tf.image.decode_jpeg(input_image)
        real_image = tf.image.decode_jpeg(real_image)
    else:
        input_image = tf.image.decode_png(input_image)
        real_image = tf.image.decode_png(real_image)

    input_image = tf.image.resize(input_image, (256, 256))
    real_image = tf.image.resize(real_image, (256, 256))

    input_image = tf.cast(input_image, tf.float32)
    real_image = tf.cast(real_image, tf.float32)
    
    return input_image, real_image

# %%

img, real = load("1.jpg")
plt.figure()
plt.imshow(img/255.0)
plt.show()

# %%
plt.figure()
plt.imshow(real/255.0)
plt.show()

# %%
