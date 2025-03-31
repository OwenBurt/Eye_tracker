'''
Author: Owen Burt
Date created: 3/31/2025
Description: A condensed version of a notebook previously uzed to process image data. 
             This script converts image data grey scale, crops the image to 170X170, stores images as numpy arrays,
             normalizes pixel values and boundry values, and stores boundries in arrays corresponding with each image.
References: 
Sources: ChatGPT, Gemini, other internet sources. 
'''

from sklearn.model_selection import train_test_split
import tensorflow as tf
import pandas as pd
import numpy as np
import os as os
import pickle
import cv2

cwd = os.getcwd()
df = pd.read_csv(cwd + '\\data\\eye_data.csv')

def view_image(image, x1, y1, x2, y2):
    ''' 
    view_image displays the bounding box on the image.

    :param image: a numpy array representing the image.
    :param x1: x min coordinates.
    :param y1: y min coordinates.
    :param x2: x max coordinates.
    :param y2: y max coordinates.
    '''

    image = image.copy()
    color = (0, 255, 0)
    thickness = 2

    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    cv2.imshow('Bounding Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = cwd + '\\image_data\\' + df['file_name'][0]
img = cv2.imread(img_path)
x1 = df['x1'][0]
y1 = df['y1'][0]
x2 = df['x2'][0]
y2 = df['y2'][0]
view_image(img, x1, y1, x2, y2)

X = df['file_name']
y = df[['x1', 'y1', 'x2', 'y2']]

train_ratio = 0.75
validation_ratio = 0.15
test_ratio = 0.10

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=1 - train_ratio)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=test_ratio/(test_ratio + validation_ratio)) 

X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)
X_val = X_val.reset_index(drop=True)
y_val = y_val.reset_index(drop=True)

img_path = cwd + '\\image_data\\' + X_train[1]
img= cv2.imread(img_path)
x1 = y_train['x1'][1]
y1 = y_train['y1'][1]
x2 = y_train['x2'][1]
y2 = y_train['y2'][1]
view_image(img, x1, y1, x2, y2)

def images_to_arr(X):
    '''
    images_to_arr gets image path, loads the image, then converts it to a 3D array. 
    
    :param X: the series of image file names to be converted.
    '''
    X_data = []
    for i in range(len(X)):
        img_path = cwd + '\\image_data\\' + X[i]
        img = cv2.imread(img_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_512x512 = cv2.resize(gray_img, (512, 512))       
        
        X_data.append(img_512x512)
    return X_data

def bounds_to_arr(y_data):
    '''
    bounds_to_arr converts boundry data from a dataframe to a np array containing just the coordinates. 
        It also normalizes the boundry values to be between 0 and 1

    :param y: the dataframe of boundry data to be converted.
    '''
    final = []
    for i in range(len(y_data)):
        df = y_data.loc[i]
        x1new = round((df['x1']/640), 2)
        y1new = round((df['y1']/360), 2)
        x2new = round((df['x2']/640), 2)
        y2new = round((df['y2']/360), 2)
        final.append((x1new, y1new, x2new, y2new))
    return np.array(final)

X_train = images_to_arr(X_train)
y_train = bounds_to_arr(y_train)
X_test = images_to_arr(X_test)
y_test = bounds_to_arr(y_test)
X_val = images_to_arr(X_val)
y_val = bounds_to_arr(y_val)

x1 = int(y_train[56][0]*512)
y1 = int(y_train[56][1]*512)
x2 = int(y_train[56][2]*512)
y2 = int(y_train[56][3]*512)
view_image((X_train[56]), x1, y1, x2, y2)

def crop_image(X_data):
    ''' 
    crop_image removes 1/3 from all sides of the image.

    :param X_data: image data as an array.
    '''
    array = []
    for i in range(len(X_data)):
        img = X_data[i]
        img_small = img[171: 341, 171: 341]
        img_norm = np.round(img_small/255, 2)
        array.append(img_norm)
    return np.array(array)

def crop_bounds(y_data):
    final = []
    for i in range(len(y_data)):
        arr = y_data[i]
        x1new = arr[0]-0.333333
        y1new = arr[1]-0.333333
        x2new = arr[2]-0.333333
        y2new = arr[3]-0.333333
        final.append((x1new, y1new, x2new, y2new))
    return np.array(final)

X_train = crop_image(X_train)
X_test = crop_image(X_test)
X_val = crop_image(X_val)
y_train = crop_bounds(y_train)
y_test = crop_bounds(y_test)
y_val = crop_bounds(y_val)

x1 = int(y_train[4][0]*512)
y1 = int(y_train[4][1]*512)
x2 = int(y_train[4][2]*512)
y2 = int(y_train[4][3]*512)
view_image(X_train[4], x1, y1, x2, y2)

data = []
data.append(X_train)
data.append(y_train)
data.append(X_test)
data.append(y_test)
data.append(X_val)
data.append(y_val)

with open('data\\data.pkl', 'wb') as file:
        pickle.dump(data, file)
