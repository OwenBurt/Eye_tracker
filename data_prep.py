''' 
Author: Owen Burt
Date created: --
Description: This code preps the data for YOLO model. This file will not work since source directory has been deleted.
             ### THIS FILE IS NO LONGER NEEDED AND HAS BEEN REPLACED BY annotations.py ###
References: --
Sources: --
'''

import pandas as pd
import numpy as np
import shutil
import os

cwd = os.getcwd()

path = cwd + "\\data\\eye_data.csv"

df = pd.read_csv(path)
shuffled_df = df.sample(frac=1).reset_index(drop=True)

def center(x1, x2, length):
    center = (x2+x1)/2
    norm = center/length
    return norm

def size(x1, x2, length):
    size = (x2-x1)/length
    return size


# Training data
for i in range(len(shuffled_df) - int(len(shuffled_df)/5)):
    row = shuffled_df.iloc[i]
    filename, ext = os.path.splitext(row['file_name'])
    sourcef = cwd + '\\image_data\\' + row['file_name']
    destf = cwd + '\\Yolo_data\\images\\train\\' + row['file_name']
    try:
        shutil.copy2(sourcef, destf)
    except:
        print('file not found')

    if (row['obj_class']=='pupil'):
        clas = 1
    else:
        clas = 0

    xc = center(row['x1'], row['x2'], 640)
    yc = center(row['y1'], row['y2'], 360)
    xs = size(row['x1'], row['x2'], 640)
    ys = size(row['y1'], row['y2'], 360)
    new_txt = np.array([clas, xc, yc, xs, ys])
    np.savetxt(cwd + '\\Yolo_data\\labels\\train\\' + filename + '.txt', new_txt.reshape(1, -1), fmt='%.5f', delimiter=' ')


# Validation data
for i in range(int(len(shuffled_df)/5)):
    index = i + (len(shuffled_df) - int(len(shuffled_df)/5))
    row = shuffled_df.iloc[index]
    filename, ext = os.path.splitext(row['file_name'])
    sourcef = cwd + '\\image_data\\' + row['file_name']
    destf = cwd + '\\Yolo_data\\images\\val\\' + row['file_name']
    try:
        shutil.copy2(sourcef, destf)
    except:
        print('file not found')
    if (row['obj_class']=='pupil'):
        clas = 1
    else:
        clas = 0

    xc = center(row['x1'], row['x2'], 640)
    yc = center(row['y1'], row['y2'], 360)
    xs = size(row['x1'], row['x2'], 640)
    ys = size(row['y1'], row['y2'], 360)
    new_txt = np.array([clas, xc, yc, xs, ys])
    np.savetxt(cwd + '\\Yolo_data\\labels\\val\\' + filename + '.txt', new_txt.reshape(1, -1), fmt='%.5f', delimiter=' ')
