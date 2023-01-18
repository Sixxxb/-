# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数汇总
np.ones((10,10),np.uint8)设置卷积核
cv2.erode(img,kernel,iterations=1)设置腐蚀的图片，核，次数
np.hstack((erosion_1,erosion_2,erosion_3))展现图片
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll4.jpg',cv2.IMREAD_COLOR)
cv_show('img',img)

#腐蚀操作
kernel=np.ones((10,10),np.uint8)    #第一个参数是卷积核的大小，数值越大腐蚀的可能性越大
erosion=cv2.erode(img,kernel,iterations=5)  #iterations是迭代次数
cv_show('erosion',erosion)

img2=cv2.imread(r'D:\OpenCvLearning\lll3.jpg',cv2.IMREAD_COLOR)
kernel2=np.ones((5,5),np.uint8)
erosion_1=cv2.erode(img2,kernel2,iterations=1)
erosion_2=cv2.erode(img2,kernel2,iterations=2)
erosion_3=cv2.erode(img2,kernel2,iterations=3)
res=np.hstack((erosion_1,erosion_2,erosion_3))
cv_show('res',res)



