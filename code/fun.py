'''声明引用库'''
from asyncio.windows_events import NULL
from contextlib import nullcontext
from importlib.resources import path
from operator import index
from tkinter import N
import cv2 as cv
from matplotlib.animation import ImageMagickBase
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

def hist_ave(hist):
    n=0
    for i in hist:
        n+=i
    return hist/n

def hist_save(hist,path,name):  #保存直方图
    plt.plot(hist,color='b')
    plt.xlim((0,256))
    plt.ylim((0,0.05))
    plt.suptitle(name,fontsize = 20, color = 'black',backgroundcolor='white')
    plt.savefig(path)
    plt.close()

def img_hist(path):  #计算直方图
    img=cv.imread(path)
    imgB=img[:,:,0]
    hist=hist_ave(cv.calcHist([img],[0],None,[256],[0,255]))
    return hist

def img_hist_no_ave(path):  #计算直方图
    img=cv.imread(path)
    imgB=img[:,:,0]
    hist=cv.calcHist([img],[0],None,[256],[0,255])
    return hist

def path_open(i):  #返回打开路径
    return 'img/'+str(i)+'.PNG'

def path_save(i):  #返回保存路径
    return 'hist/'+str(i)+'_HIST.jpg'

def hist_name(i):  #返回直方图标题
    return 'HIST_'+str(i)

def csv_save(data,path,name):  #保存csv文件
    path=path+'/'+name+'.csv'
    f=open(path,'a+')
    f.write(data)
    f.close()

def gray_index(hist):
    n=0
    j=1
    for i in hist:
        n=n+i*j
        j+=1
    return str(n/1228800)

def hist_avea(input,output,n):
    histSum=NULL
    for i in tqdm(range(n)):
        hist=img_hist(path_open(i))
        histSum+=hist
    hist=hist_ave(histSum)
    hist_save(hist,'HIST_AVE.jpg','HIST_AVE')
    print('Average Histogram Completed!')
    n=0
    for i in hist:
        n+=1
        csv_save(str(n)+','+str(i)[1:-2]+'\n','.','HIST_AVE')
    print('Average Histogram Exported!')

def hist_single(input,output,n):
    for i in tqdm(range(n)):
        hist=img_hist(path_open(i))
        hist=hist_ave(hist)
        hist_save(hist,path_save(i),hist_name(i))
    print('Single Histogram Completed!')

def gray_index(input,ouput,n):
    num=0
    sum=0
    for i in tqdm(range(n)):
        hist=img_hist_no_ave(path_open(i))
        csv_save(str(num)+','+gray_index(hist)[1:-1]+'\n','.','index')
        sum+=gray_index(hist)[1:-1]
        num+=1
    csv_save('AVE,'+gray_index(hist)[1:-1]+'\n','.','index')
    print('Single Gray Exported!')
    print('')

