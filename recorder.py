import mss
import cv2
import numpy as np



resolution = (1920, 1080)
fps = 30.0

monitor = {"top": 0, "left": 0, "width": resolution[0], "height": resolution[1]}
sct = mss.mss()

output_filename = "recording.avi"

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)


recording_has_started = False
recording_has_finished = False

while not recording_has_finished:
	if recording_has_started:
		img = sct.grab(monitor)
		frame = np.array(img)

		# Convert it from BGR to RGB
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		# Write it to the output file
		out.write(frame)

		cv2.imshow('Live', frame)

		# Stop recording when we press 'q'
		if cv2.waitKey(1) == ord('q'):
			recording_has_finished = True

	elif cv2.waitKey(1) == ord('s'):
		recording_has_started = True
	

# Release the Video writer
out.release()
 
# Destroy all windows
cv2.destroyAllWindows()
