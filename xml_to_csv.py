'''
Author: Owen Burt
Date created: 2/20/2025
Description: This file converts image annotations from the xml files produced by an image labeler to a csv.
References: I referenced Chatura Wijetunga's object detection project as en example and for inspiration.
Sources: Chatura Wijetunga: https://medium.com/nerd-for-tech/building-an-object-detector-in-tensorflow-using-bounding-box-regression-2bc13992973f
'''

import numpy as np
import pandas as pd

#Importing .png and .XML files.
