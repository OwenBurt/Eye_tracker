'''
Author: Owen Burt
Date created: 4/20/2025
Description: This file extracts data from xml annotation files and creates new .txt files for YOLO v11. 
             These files are stored in data/labels/*. The corresponding image files are then moved from image_data to data/images/*.
References: I referenced Chatura Wijetunga's object detection project as en example and for inspiration.
Sources: Chatura Wijetunga: https://medium.com/nerd-for-tech/building-an-object-detector-in-tensorflow-using-bounding-box-regression-2bc13992973f
'''

import xml.etree.ElementTree as ET
import random
import shutil
import glob
import os

#Gathering .XML file paths from image_data directory
cwd = os.getcwd()
files = glob.glob(cwd + '/image_data/*.xml')

#class_id x_center y_center width height

def check_id(name):
    if (name == 'pupil'):
        return 1
    else:
        return 0
    
random.shuffle(files)
split = int(len(files)*0.75)

def create_txt(files, file_location):

    if (file_location == 'train'):
        length = split
        place_holder = 0
    elif (file_location == 'val'):
        length = len(files) - split
        place_holder = split
    else:
        raise ValueError("Invalid input: Path does not exist")
    
    for i in range(length):
        file_path = files[i+place_holder]
        contents = (ET.parse(file_path)).getroot()        
        file = contents.find('filename').text
        file_name, ext = os.path.splitext(file)
        class_name = contents.find('object/name').text

        x1 = int(contents.find('object/bndbox/xmin').text)
        y1 = int(contents.find('object/bndbox/ymin').text)
        x2 = int(contents.find('object/bndbox/xmax').text)
        y2 = int(contents.find('object/bndbox/ymax').text)

        class_id = check_id(class_name)
        x_center = round(((x1+x2)/2)/640, 6)
        y_center = round(((y1+y2)/2)/360, 6)
        width = round((x2-x1)/640, 6)
        height = round((y2-y1)/360, 6)

        with open(cwd + '\\data\\labels\\' + file_location + '\\' + file_name + '.txt', 'w') as new_file:
            new_file.write(str(class_id) + " " + str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height))

        shutil.move(cwd + '\\image_data\\' + file_name + '.jpg', cwd + '\\data\\images\\' + file_location + '\\' + file_name + '.jpg')

create_txt(files, 'train')
create_txt(files, 'val')
