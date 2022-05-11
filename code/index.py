from tkinter import Menu
import cv2 as cv
import numpy as np
from tqdm import tqdm

def csv_save(n,mean,dev):
    f=open('index.csv','a')
    data=str(n)+','+str(mean)+','+str(dev)+'\n'
    f.write(data)
    f.close()

def index(n):
    path=str('img/'+str(n)+'.PNG')
    img=cv.imread(path,0)
    mean,dev=cv.meanStdDev(img)
    mean=round(float(mean),4)
    dev=round(float(dev),4)
    csv_save(n,mean,dev)
    return mean,dev

def ave(l):
    sum=0
    for i in l:
        sum+=i
    return sum/len(l)
    

def main(n):
    meanAll=[]
    devAll=[]
    csv_save('n','mean','dev')
    for i in tqdm(range(n)):
        mean,dev=index(i)
        meanAll.append(mean)
        devAll.append(dev)
    meanAve=ave(meanAll)
    devAve=ave(devAll)
    csv_save('ave',str(meanAve),str(devAve))
    

main(75)






