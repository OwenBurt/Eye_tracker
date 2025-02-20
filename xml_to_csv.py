'''
Author: Owen Burt
Date created: 2/20/2025
Description: This file converts image annotations from the xml files produced by an image labeler to a csv.
References: I referenced Chatura Wijetunga's object detection project as en example and for inspiration.
Sources: Chatura Wijetunga: https://medium.com/nerd-for-tech/building-an-object-detector-in-tensorflow-using-bounding-box-regression-2bc13992973f
'''

import numpy as np
import pandas as pd
import glob
import xml.etree.ElementTree as ET

#Importing .png and .XML files from annotated_images folder.
files = glob.glob('annotated_images/*')

#Parsing out xml and storing it in dataframe.
for i in range(1, len(files), 2):
    contents = (ET.parse(files[1])).getroot()
    img_name = contents.find('filename').text
    img_height = contents.find('height').text
    img_width = contents.find('width').text
    img_name = contents.find('name').text
    x1 = contents.find('xmin').text
    y1 = contents.find('ymin').text
    x2 = contents.find('xmax').text
    y2 = contents.find('ymax').text


