'''
Author: Owen Burt
Date created: 2/27/2025
Description: 
    This file adds annotations to negative files in .xml files and stores them in the image_data directory.
    The structure for these annotation files replicates the structure that labelimg produces. 
    *** After this code was run I moved the negative images to image_data and deleted      ***
    *** the seperate directory containing my negative images that was called to_be_labeled ***
References: 
Sources: 
   1. Stack Overflow https://stackoverflow.com/questions/3605680/creating-a-simple-xml-file-using-python
   2. Python Docs https://docs.python.org/3/library/xml.etree.elementtree.html
'''

import xml.etree.cElementTree as ET
import glob
import os

cwd = os.getcwd()

files = glob.glob(cwd + '/to_be_labeled/*') # This directory no longer exits

for file in files:
    file_name = os.path.basename(file)
    file_name_xml =  os.path.splitext(file_name)[0] + '.xml'
    annotation = ET.Element('annotation')
    folder = ET.SubElement(annotation, 'folder').text = 'to_be_labeled'
    filename = ET.SubElement(annotation, 'filename').text = file_name
    path = ET.SubElement(annotation, 'path').text = file
    source = ET.SubElement(annotation, 'source')
    database = ET.SubElement(source, 'database').text = 'Unknown'
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width').text = '640'
    height = ET.SubElement(size, 'height').text = '360'
    depth = ET.SubElement(size, 'depth').text = '1'
    segmented = ET.SubElement(annotation, 'segmented').text = '0'
    object = ET.SubElement(annotation, 'object')
    name = ET.SubElement(object, 'name').text = 'negative'
    pose = ET.SubElement(object, 'pose').text = 'Unspecified'
    truncated = ET.SubElement(object, 'truncated').text = '0'
    difficult = ET.SubElement(object, 'difficult').text = '0'
    bndbox = ET.SubElement(object, 'bndbox')
    xmin = ET.SubElement(bndbox, 'xmin').text = '0'
    ymin = ET.SubElement(bndbox, 'ymin').text = '0'
    xmax = ET.SubElement(bndbox, 'xmax').text = '0'
    ymax = ET.SubElement(bndbox, 'ymax').text = '0'
    tree = ET.ElementTree(annotation)
    ET.indent(tree, '   ')
    tree.write(cwd + '/image_data/' + file_name_xml)