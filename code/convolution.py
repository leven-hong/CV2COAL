import cv2 as cv
import numpy as np


img=cv.imread('img/30.PNG',0)
padImg=cv.copyMakeBorder(img,1,1,1,1,cv.BORDER_CONSTANT,0)

kernel=np.array([
    [1,1,1],
    [1,-4,1],
    [1,1,1]
])
dst=cv.filter2D(padImg,-1,kernel)

cv.imshow('cons',dst)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('123.jpg',dst)