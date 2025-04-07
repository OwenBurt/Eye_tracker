'''
Author: Owen Burt
Date created: 2/20/2025
Description: This script converts image annotations from the xml files produced by an image labeler to a csv called eye_data.csv.
References: I referenced Chatura Wijetunga's object detection project as en example and for inspiration.
Sources: Chatura Wijetunga: https://medium.com/nerd-for-tech/building-an-object-detector-in-tensorflow-using-bounding-box-regression-2bc13992973f
'''

import xml.etree.ElementTree as ET
import pandas as pd
import glob
import os

#Gathering .XML file paths from image_data directory
cwd = os.getcwd()
files = glob.glob(cwd + '/image_data/*.xml') #this directory no longer exists

list = []
for file_path in files:

    contents = (ET.parse(file_path)).getroot()        
    file_name = contents.find('filename').text        
    obj_class = contents.find('object/name').text        
    x1 = contents.find('object/bndbox/xmin').text
    y1 = contents.find('object/bndbox/ymin').text
    x2 = contents.find('object/bndbox/xmax').text
    y2 = contents.find('object/bndbox/ymax').text
    data = {'file_name':file_name, 'obj_class':obj_class, 'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}
    list.append(data)

final_df = pd.DataFrame(list)
final_df.to_csv('data\\eye_data.csv', index=False)

exit(0)