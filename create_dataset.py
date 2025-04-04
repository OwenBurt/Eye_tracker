'''
Author: Owen Burt
Date created: 3/31/2025
Description: A condensed version of a notebook previously used to process image data. 
             This script converts image data grey scale, stores images as arrays,
             normalizes pixel values and boundry values, and stores boundries in arrays corresponding with each image.
References: 
Sources: ChatGPT, Gemini, other internet sources. 
'''

import pandas as pd
import numpy as np
import os as os
import pickle
import cv2

cwd = os.getcwd()
df = pd.read_csv(cwd + '\\data\\eye_data.csv')