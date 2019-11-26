import cv2
from matplotlib import pyplot as plt

print(cv2.__version__)

# Read an image
path = "/home/tim/PycharmProjects/CVFinalProject/GoogleColab/Images/17_00000001.jpg"
img = cv2.imread(path, flags=1) # flags (0=grayscale, 1=color in BGR not RGB)

# Display an image with imshow
cv2.namedWindow('image', cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL makes image resizable
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display an image with matplotlib
img2 = img[:, :, ::-1] # matplot lib uses RGB but opencv uses BGR so we need to flip the red and blue channels

plt.figure(figsize=(10,10))
plt.subplot(211)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.title("BGR (opencv default)")
# plt.show()

plt.subplot(212)
plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.title("RGB")
plt.show()