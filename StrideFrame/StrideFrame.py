import cv2
import os

path = "output.mp4"
cap = cv2.VideoCapture(path)
count = 0
os.makedirs("Frames", exist_ok=True)

fps = int(cap.get(cv2.CAP_PROP_FPS))
stride = int(input("Gap between Frames(Sec): "))
frame_interval = fps * stride

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if count % frame_interval == 0:
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Get the timestamp in seconds
        time_str = "{:.2f}".format(timestamp)  # Format the timestamp as a string with 2 decimal places
        cv2.imwrite("Frames/frame_{}.jpg".format(time_str), frame)
        print("Result saved to Frames")

    count += 1

cap.release()
