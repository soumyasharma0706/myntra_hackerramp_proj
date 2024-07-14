import cv2
import numpy as np

# Load the original image
original_image = cv2.imread('input/03615_00.jpg')

# Load the mask image (assuming it's a binary mask with white areas to be colored red)
mask_image = cv2.imread('output/alpha/1.png', cv2.IMREAD_GRAYSCALE)

# Ensure mask is binary (values should be 0 or 255)
_, binary_mask = cv2.threshold(mask_image, 127, 255, cv2.THRESH_BINARY)

# Create a red version of the original image where mask is white
red_image = original_image.copy()
red_image[binary_mask == 255] = [0, 0, 255]  # BGR format for red

# Save the result
cv2.imwrite('path/to/result_image.jpg', red_image)

# Optionally, display the result
cv2.imshow('Result', red_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
