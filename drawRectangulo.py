import cv2
import numpy as np

ix = -1
iy = -1
dibujando = False

def draw_rectangle(event, x, y, flags, params):
    global ix, iy, dibujando

    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 152, 231), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 152, 231), -1)

img = np.zeros((512, 512, 3), dtype="uint8")

cv2.namedWindow(winname='mi dibujo')
cv2.setMouseCallback('mi dibujo', draw_rectangle)

while True:
    cv2.imshow('mi dibujo', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

        cv2.destroyAllWindow()