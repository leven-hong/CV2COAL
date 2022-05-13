import numpy as np
import cv2 as cv


def watershed(imgpath):
    img = cv.imread(imgpath)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret0, thresh0 = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh0,cv.MORPH_OPEN,kernel, iterations = 2)

    # 确定背景区域
    sure_bg = cv.dilate(opening,kernel,iterations=3)

    # 确定前景区域
    dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
    ret1, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # 查找未知区域
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg,sure_fg)

    # 标记标签
    ret2, markers1 = cv.connectedComponents(sure_fg)
    markers = markers1+1
    markers[unknown==255] = 0

    markers3 = cv.watershed(img,markers)
    img[markers3 == -1] = [0,255,0]
    return thresh0,sure_bg,sure_fg,img

if __name__ == '__main__':
    imgpath = '123.jpg'
    thresh0, sure_bg, sure_fg, img = watershed(imgpath)

    cv.imshow('thresh0',thresh0)
    cv.imshow('sure_bg', sure_bg)
    cv.imshow('sure_fg', sure_fg)
    cv.imshow('result_img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()