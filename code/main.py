from function import *
from tqdm import tqdm
import numpy as np


def main(n):
    histAll=[]
    dHistAll=[]
    sHistAll=[]
    for i in tqdm(range(n)):
        hist=hist_cal('img/'+str(i)+'.PNG')
        histAll.append(hist)
        hist_save(hist,'hist/'+str(i)+'.jpg')

        dHist=d_hist(hist)
        dHistAll.append(dHist)
        hist_save(dHist,'hist_d/'+str(i)+'.jpg')

        sHist=s_hist(hist)
        sHistAll.append(sHist)
        hist_save(sHist,'hist_s/'+str(i)+'.jpg')
    histSum=np.sum(histAll,axis=0)
    hist_save(histSum,'HIST.jpg')
    dHistSum=np.sum(dHistAll,axis=0)
    hist_save(dHistSum,'HIST_d.jpg')
    sHistSum=np.sum(sHistAll,axis=0)
    hist_save(sHistSum,'HIST_s.jpg')

    


main(75)