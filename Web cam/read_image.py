# images are stores as pixels having BGR value in cv2
import cv2
array = cv2.imread("image.png")
print(array)
print(array.shape) # result is (pixels horizantally, pixels vertically, channels)