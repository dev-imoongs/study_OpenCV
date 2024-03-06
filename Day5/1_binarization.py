import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

# _: 설정한 threshold값
_, dst1 = cv2.threshold(hist, 100, 255, cv2.THRESH_BINARY)
_, dst2 = cv2.threshold(hist, 210, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

plt.plot(hist)
plt.show()

cv2.waitKey()




