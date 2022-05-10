from platform import release
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt




img=cv.imread('coke/3.bmp',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
    
    # 这里构建振幅图的公式没学过
magnitude_spectrum = 20*np.log(np.abs(fshift))#先取绝对值,表示取模。取对数,将数据范围变小 

plt.imshow(magnitude_spectrum , cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.savefig('coke/3.jpg')
print('Fast Fourier Fransform Completed!')