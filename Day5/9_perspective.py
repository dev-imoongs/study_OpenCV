import cv2
import numpy as np

img = cv2.imread('./pic.jpg')
w, h = 600, 400

srcQuad = np.array([[370, 173], [1220, 155], [1420, 840], [210, 850]], np.float32)
dstQuad = np.array([[0, 0], [w, 0], [w, h], [w, 0]], np.float32)

print('srcQuad:', srcQuad)
print('dstQuad:', dstQuad)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(img, pers, (w, h))

cv2.imshow('dst', dst)
cv2.waitKey()