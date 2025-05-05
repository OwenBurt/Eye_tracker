'''
Author: Owen Burt
Date created: 4/26/2025
Description: This file tests the best model trained on my_bad_model. 
References: ChatGPT, I have very little experience with OpenCV and used ChatGPT to help narrow down the functions and parameters needed. 
Sources: ChatGPt.
'''

import tensorflow as tf
import numpy as np
import cv2
import os

cwd = os.getcwd()
model_file = cwd + '\\my_models\\my_model5.h5'

model = tf.keras.models.load_model(model_file)

cap = cv2.VideoCapture(1)

window_name = 'MY_MODEL'

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

while True:
    ret, frame = cap.read()
    if not ret:
        break
   
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (512, 512)) 
    frame = frame[171: 341, 171: 341]
    frame = np.expand_dims(frame, axis=-1)  
    frame = np.expand_dims(frame, axis=0) 
    frame = frame / 255.0 

    results = model.predict(frame)

    x1 = int(results[0][0]*512)
    y1 = int(results[0][1]*512)
    x2 = int(results[0][2]*512)
    y2 = int(results[0][3]*512)

    frame_to_show = frame[0]
    cv2.rectangle(frame_to_show, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow(window_name, frame_to_show)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
