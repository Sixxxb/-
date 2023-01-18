# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)寻找梯度所在位置
cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll4.jpg',cv2.IMREAD_GRAYSCALE)
cv_show('img',img)
"""函数原型
dst=cv2.Sobel(src,ddepth,dx,dy,ksize)
src:源图像
ddepth:图像深度,当depth=-1时,输出图像会具有和源图像相同的深度。因此一般都是-1
dx,dy:图像方向水平/竖直
ksize:Sobel算子大小,一般都是3(3*3)
"""
#x,y方向分别算子
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely=cv2.convertScaleAbs(sobely)

#x,y方向求和,即将两个图像叠加用addWeighted函数
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

plt.subplot(221),plt.imshow(img),plt.title('img')
plt.subplot(222),plt.imshow(sobelx),plt.title('sobelx')
plt.subplot(223),plt.imshow(sobely),plt.title('sobely')
plt.subplot(224),plt.imshow(sobelxy),plt.title('sobelxy')
plt.show()

#实例:人的轮廓线的展示
img1=cv2.imread(r'D:\OpenCvLearning\lll6.jpg',cv2.IMREAD_GRAYSCALE)
#cv_show('img',img)
img1_sobelx=cv2.Sobel(img1,cv2.CV_64F,1,0,ksize=3)
img1_sobelx=cv2.convertScaleAbs(img1_sobelx)
img1_sobely=cv2.Sobel(img1,cv2.CV_64F,0,1,ksize=3)
img1_sobely=cv2.convertScaleAbs(img1_sobely)
img1_sobelxy=cv2.addWeighted(img1_sobelx,0.5,img1_sobely,0.5,0)
#cv_show('sobelxy',sobelxy)
plt.subplot(121),plt.imshow(img1),plt.title('img1')
plt.subplot(122),plt.imshow(img1_sobelxy),plt.title('img1_sob')
plt.show()