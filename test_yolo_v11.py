'''
Author: Owen Burt
Date created: 4/26/2025
Description: This file tests the best model trained on YOLO v11. 
References: ChatGPT, The majority of this code is from ChatGPT
Sources: I used ChatGPT to give me the OpenCV (cv2) funcions to open video feed and alter it by adding bounding boxes.
'''

from ultralytics import YOLO
import cv2

model_file = 'C:\\Users\\owend\\Projects\\Eye_tracker\\runs\\detect\\train2\\weights\\best.pt'

model = YOLO(model_file)

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose = False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            conf = float(box.conf[0])                         
            cls = int(box.cls[0])                            
            label = model.names[cls]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('YOLOv11 Model', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()