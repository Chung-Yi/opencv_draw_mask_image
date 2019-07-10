import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        cv2.circle((img_mask), (x, y), 5, (255, 255, 255), -1)


img = cv2.imread('test.jpg')
h, w, _ = img.shape
img_mask = np.zeros((h, w), dtype=np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('mask.jpg', img_mask)
cv2.destroyAllWindows()