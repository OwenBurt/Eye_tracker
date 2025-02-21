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
import os

#This function handles annotated images
def parse_anotated_files(files, df):
    for i in range(len(files)):
        contents = (ET.parse(files[i])).getroot()
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
    for i in range(len(files)):
        file_name = files[i]
        print(file_name)
        obj_class = "NEGATIVE"
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
    df = df.append({'file_name':file_name, 'obj_class':obj_class, 'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2})

#Getting current working directory
cwd = os.getcwd()

#Importing .png and .XML files from annotated_images folder
anotated_img_files = glob.glob(cwd+"anotated_images/*.xml")

#Parsing out xml and storing it in dataframe
anotated_img_df = pd.DataFrame()

#Importing .png files from negative_images folder
negative_img_files = glob.glob(cwd+"negative_images/*.jpg")
print(negative_img_files)
#Adding the negative image data to a dataframe
negative_img_df = pd.DataFrame()

#calling functions
try:
    anotated_df = parse_anotated_files(anotated_img_files, anotated_img_df)
    print("Anotated images successful")
except:
    print("Error converting annotated images")

try:
    negative_df = negative_images(negative_img_files, negative_img_df)
    print("Negative images successful")
except:
    print("Error adding negative files")

final_df = pd.concat([anotated_df, negative_df])
final_df.to_csv('eye_data.csv', index=False)

exit(0)