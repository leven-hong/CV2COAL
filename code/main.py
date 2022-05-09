from asyncio.windows_events import NULL
from contextlib import nullcontext
from importlib.resources import path
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

def hist_save(hist,path,name):  #保存直方图
    plt.plot(hist,color='b')
    plt.xlim((0,256))
    plt.ylim((0,0.03))
    plt.suptitle(name,fontsize = 20, color = 'black',backgroundcolor='white')
    plt.savefig(path)
    plt.close()

def img_hist(path):  #计算直方图
    img=cv.imread(path,0)
    hist=cv.calcHist([img],[0],None,[256],[0,255])
    n=0
    for i in hist:
        n+=i
    return hist/n

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

def main(input,output,n,mode):  #主函数，mode为1时保存单个直方图
    #遍历并生成单个直方图
    hist_all=[]
    hist_sum=NULL
    for i in tqdm(range(n)):
        hist=img_hist(path_open(i))
        hist_all.append(hist)
        hist_sum+=hist
        if mode==1:
            hist_save(hist,path_save(i),hist_name(i))
    if mode==1:
        print('Single Histogram Completed!')
        
    #计算并保存平均直方图
    n=0
    for i in tqdm(hist_sum):
        n+=i
    hist_ave=hist_sum/n
    hist_save(hist_ave,'HIST_AVE.jpg','HIST_AVE')

    #保存平均直方图信息
    n=0
    for i in hist_ave:
        n+=1
        csv_save(str(n)+','+str(i)[1:-2]+'\n','.','HIST_AVE')
    print('Average Histogram Completed!')
    


