# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数汇总
cv2.dilate(img,kernel,iterations=5)图像膨胀运算
cv2.erode(img,kernel,iterations=5)图像腐蚀运算
cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)图像梯度运算
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll.jpg',cv2.IMREAD_COLOR)
img1=cv2.imread(r'D:\OpenCvLearning\lll4.jpg',cv2.IMREAD_COLOR)
cv_show('img',img)
cv_show('img1',img1)

#梯度=膨胀-腐蚀(图像的减法)，可以获取图像的轮廓信息
kernel=np.ones((3,3),np.uint8)
dilate=cv2.dilate(img,kernel,iterations=5)
erosion=cv2.erode(img,kernel,iterations=5)
res=np.hstack((dilate,erosion))
cv_show('res',res)

#通过cv2.MORPH_GRADIENT来实现图像的梯度运算
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)    #梯度运算函数
gradient1=cv2.morphologyEx(img1,cv2.MORPH_GRADIENT,kernel)    #梯度运算函数
cv_show('gradient',gradient)
cv_show('gradient1',gradient1)

