
import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./taekwonv1.jpg')
img2 = cv2.imread('./taekwonv2.jpg')
img3 = cv2.imread('./taekwonv3.jpg')
img4 = cv2.imread('./dr_ochanomizu.jpg')

imgs = [img1, img2, img3, img4]
hists = []

for i, img in enumerate(imgs):
    plt.subplot(1, len(imgs), i+1)
    plt.title('img%d' % (i+1))
    plt.axis('off')
    plt.imshow(img[:, :, ::-1])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])