import cv2
import numpy as np

#Read input file
image = cv2.imread("rice_fields.jpg")

# convert to hsv (hue, saturation, value)
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# choose desired of green range to mask (36,25,25) ~ (86, 255,225)
mask = cv2.inRange(HSV, (36, 25, 25), (75, 255,255))

# slice green colour within image
image_mask = mask>0
green = np.zeros_like(image, np.uint8)
green[image_mask] = image[image_mask]

# save the output file
cv2.imwrite("rice_fields_green.png", green)
