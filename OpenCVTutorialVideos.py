import cv2
from matplotlib import pyplot as plt

print(cv2.__version__)

# Read a Video
path = "/home/tim/PycharmProjects/CVFinalProject/GoogleColab/Videos/Study clip 019.mpg"
cap = cv2.VideoCapture(path) # 0 to n for camera, or filepath as a string for existing video
# ret = cap.set(3,cap.get(3) * 2) # double width
# ret = cap.set(4,cap.get(4) * 2) # double height
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break
    # Our operations on the frame come here
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()