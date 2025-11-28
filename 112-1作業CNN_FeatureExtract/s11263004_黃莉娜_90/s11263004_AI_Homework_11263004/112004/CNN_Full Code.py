import numpy as np
import cv2

# Load the image
#image = cv2.imread(r'AI_Homework\1.png')
image = cv2.imread('1.png')


# 直線
kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# 橫線
kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# 斜線
kernel_z = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

# Apply the convolution filter
result_x = cv2.filter2D(image, -1, kernel_x)
result_y = cv2.filter2D(image, -1, kernel_y)
result_z = cv2.filter2D(image, -1, kernel_z)

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Vertical", result_x)
cv2.imshow("Horizontal", result_y)
cv2.imshow("Slash", result_z)
cv2.waitKey(0)
cv2.destroyAllWindows()