import pyautogui
import cv2
import numpy as np


resolution = (1920, 1080)
fps = 30.0

output_filename = "recording.avi"

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
	img = pyautogui.screenshot()
	frame = np.array(img)

	# Convert it from BGR to RGB
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)

	cv2.imshow('Live', frame)

	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()
 
# Destroy all windows
cv2.destroyAllWindows()
