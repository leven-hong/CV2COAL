from function import *

hist=hist_cal('img/1.PNG')

hist_save(hist,'1.jpg')
dHist=d_hist(hist)
hist_save(dHist,'2.jpg')
sHist=s_hist(hist)
hist_save(sHist,'3.jpg')
