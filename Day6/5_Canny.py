import cv2
import numpy as np

img = cv2.imread('./dog.bmp')
med_val =  np.median(img)
lower = int(max(0, 0.7*med_val))
upper = int(min(255, 1.3*med_val))

print(lower, upper)

dst = cv2.GaussianBlur(img, (3, 3), 0, 0)
dst = cv2.Canny(dst, lower, upper, 3)

cv2.imshow('dst1', img)
cv2.imshow('dst2', dst)
cv2.waitKey()