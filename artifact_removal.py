import cv2
from matplotlib import pyplot as plt
import numpy as np

original_image = cv2.imread("C:/Semester4/digital_image_processing/dip_project/images/original_image.jpg")

marked_image = cv2.imread("C:/Semester4/digital_image_processing/dip_project/images/marked_image.jpg",0)
plt.imshow(marked_image, cmap='gray')
plt.title('Marked Image')
plt.show()

ret , thresh = cv2.threshold(marked_image, 254, 255, cv2.THRESH_BINARY)
plt.imshow(thresh, cmap='gray')
plt.title('Mask Threshold')
plt.show()


kernel = np.ones((7, 7), np.uint8)

mask = cv2.dilate(thresh, kernel, iterations = 1)
plt.imshow(mask, cmap='gray')
plt.title('Mask')
plt.show()

restored_image = cv2.inpaint(original_image, mask, 3, cv2.INPAINT_TELEA)
plt.imshow(restored_image)
plt.title('Restored_Image')
plt.show()

cv2.imwrite("./images/Restored_shivaji.jpg", restored_image)