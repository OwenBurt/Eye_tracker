'''

Author: Owen Burt
Date created: 4/26/2025
Description: This file tests the best model trained on my_bad_model. 
References: ChatGPT, The majority of this code is from ChatGPT
Sources: I used ChatGPT to give me the OpenCV (cv2) funcions to open video feed and alter it by adding bounding boxes.
'''

import tensorflow as tf
import numpy as np
import cv2
import os

cwd = os.getcwd()
model_file = cwd + '\\my_models\\my_bad_model6.h5'

model = tf.keras.models.load_model(model_file)

cap = cv2.VideoCapture(1)

window_name = 'MY_BAD_MODEL :('

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