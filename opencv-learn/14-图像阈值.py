# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)灰度化图片
cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)设置阈值函数
plt.xticks([]),plt.yticks([])绘图时不使用标尺
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll8.jpg',cv2.IMREAD_COLOR)
#灰度化
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#利用函数ret,dst=cv2.threshold(src,thresh,maxval,type)
"""
src:输入图，只能输入单通道图像，通常为灰度图
dst:输出图
thresh:阈值
maxval:当像素超过了阈值(或者小于阈值，根据type来决定),所赋予的值,一般是255
type:二值化操作的类型，包含以下五种:
    cv2.THRESH_BINARY：二值化,超过阈值部分取maxval,否则取0
    cv2.THRESH_BINARY_INV：二值化(THRESH_BINARY)反转
    cv2.THRESH_TRUNC：四值化,大于阈值部分设为阈值,否则不变
    cv2.THRESH_TOZERO：大于阈值部分不改变,否则设为0
    cv2.THRESH_TOZERO_INV：取值为0(THRESH_TOZERO)反转
"""
ret,thresh1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)

titles=['Original Image', 'BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])   #控制图片下面的分辨率标尺,[]为不使用标尺
plt.show()