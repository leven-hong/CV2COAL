import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from tqdm import tqdm
np.set_printoptions(suppress=True)

def hist_cal(path):
    img=cv.imread(path)
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    hist=cv.calcHist([img_gray],[0],None,[256],[0,255])
    l=[]
    hist=hist.tolist()
    for i in hist:
        l.append(int(i[0]))
    return l

def hist_save(hist,path):
    n=len(hist)
    x=[]
    for i in range(n):
        x.append(i)
    plt.plot(x,hist,color='b')
    plt.savefig(path)
    plt.close()

def d_hist(hist):
    dHist=[]
    for i in range(len(hist)):
        dHist.append(hist[i]-hist[i-1])
    return dHist

def s_hist(hist):
    sHist=[]
    sHist.append(hist[0])
    for i in hist[1:]:
        sHist.append(sHist[-1]+i)
    return(sHist)

