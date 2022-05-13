from re import L
from turtle import color
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from tqdm import tqdm
np.set_printoptions(suppress=True)

def build_list():   #建立x轴
    l=[]
    for i in range(256):
        l.append(i)
    return l

def hist_cal(path): #输入路径返回灰度图列表
    img=cv.imread(path)
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    hist=cv.calcHist([img_gray],[0],None,[256],[0,255])
    l=[]
    hist=hist.tolist()
    for i in hist:
        l.append(int(i[0]))
    return l

def hist_save(x,hist,path): #折线图保存
    plt.plot(x,hist,color='b')
    plt.axvline(30,color='r')
    plt.savefig(path)
    plt.close()

def d_hist(hist):   #直方图一阶导
    dHist=[]
    for i in range(len(hist)):
        dHist.append(hist[i]-hist[i-1])
    return dHist

def s_hist(hist):   #直方图一阶积分
    sHist=[]
    sHist.append(hist[0])
    for i in hist[1:]:
        sHist.append(sHist[-1]+i)
    return(sHist)

def main(n):
    histAll=[]
    dHistAll=[]
    sHistAll=[]
    l=build_list()

    for i in tqdm(range(n)):
        hist=hist_cal('img/'+str(i)+'.PNG')
        histAll.append(hist)
        hist_save(l,hist,'hist/'+str(i)+'.jpg')

        dHist=d_hist(hist)
        dHistAll.append(dHist)
        hist_save(l,dHist,'hist_d/'+str(i)+'.jpg')

        sHist=s_hist(hist)
        sHistAll.append(sHist)
        hist_save(l,sHist,'hist_s/'+str(i)+'.jpg')
    
    
    histSum=np.sum(histAll,axis=0)
    hist_save(l,histSum,'HIST.jpg')
    dHistSum=np.sum(dHistAll,axis=0)
    hist_save(l,dHistSum,'HIST_d.jpg')
    sHistSum=np.sum(sHistAll,axis=0)
    hist_save(l,sHistSum,'HIST_s.jpg')
    
    

main(75)
