'''
Author: Owen Burt
Date created: 2/20/2025
Description: This file converts image annotations from the xml files produced by an image labeler to a csv.
References: I referenced Chatura Wijetunga's object detection project as en example and for inspiration.
Sources: Chatura Wijetunga: https://medium.com/nerd-for-tech/building-an-object-detector-in-tensorflow-using-bounding-box-regression-2bc13992973f
'''

import pandas as pd
import glob
import xml.etree.ElementTree as ET

#This function handles annotated images
def parse_annotated_files(files, df):
    for i in range(1, len(files), 2):
        contents = (ET.parse(files[1])).getroot()
        file_name = contents.find('filename').text 
        obj_class = contents.find('name').text
        x1 = contents.find('xmin').text
        y1 = contents.find('ymin').text
        x2 = contents.find('xmax').text
        y2 = contents.find('ymax').text
        df = df.append({'file_name':file_name, 'obj_class':obj_class, 'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2})
    return df

#This function handles negtive images
def negative_images(files, df):
    for i in files:
        file_name = i
        obj_class = "NEGATIVE"
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
    df = df.append({'file_name':file_name, 'obj_class':obj_class, 'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2})


#Importing .png and .XML files from annotated_images folder
annotated_img_files = glob.glob('annotated_images/*')

#Parsing out xml and storing it in dataframe
annotated_img_df = pd.DataFrame()

#Importing .png files from negative_images folder
negative_img_files = glob.glob('negative_images/*')

#Adding the negative image data to a dataframe
negative_img_df = pd.DataFrame()

#calling functions
try:
    annotated_df = parse_annotated_files(annotated_img_files, annotated_img_df)
    print("Annotated images successful")
except:
    print("Error converting annotated images")

try:
    negative_df = negative_images(negative_img_files, negative_img_df)
    print("Negative images successful")
except:
    print("Error adding negative files")

