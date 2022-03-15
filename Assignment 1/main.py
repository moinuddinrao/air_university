import imageio as io
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Original Image
image = io.imread('mrincredible.jpg')
plt.imshow(image)
plt.show()


# Load a colored image in grayscale
img1 = cv2.imread('mrincredible.jpg', 0)
plt.imshow(img1, cmap='gray', interpolation='bicubic')
plt.show()
 
# converting to gray scale manually
img2 = io.imread('propeller.jpg')
row, col, channel = img2.shape

gray = np.zeros((row, col))

for i in range(row):
    for j in range(col):
        gray[i, j] = img2[i, j, 0] * 0.2989 + img2[i, j, 1] * 0.5870 + img2[i, j, 2] * 0.1140

plt.imshow(gray, cmap='gray')
plt.show()

# converting obtained gray image to binary image

# define a threshold, 128 is the middle of black and white in grey scale

# threshold the image
bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('Binary', bw)
cv2.waitKey(0)
cv2.destroyAllWindows()