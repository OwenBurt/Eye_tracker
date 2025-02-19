import cv2

# Open the default camera (index 0)
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Unable to access the camera.")
    exit()

print("Press 'q' to quit the video feed.")

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Failed to grab a frame.")
        break

    # Display the video feed
    cv2.imshow("Camera Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()