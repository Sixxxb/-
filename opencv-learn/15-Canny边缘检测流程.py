# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.Canny(img,80,150)Canny边缘检测函数
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll8.jpg',cv2.IMREAD_GRAYSCALE)

"""
Canny边缘检测
1.使用高斯滤波器，以平滑图像，滤除噪声
2.计算图像中每个像素点的梯度强度和方向
3.应用非极大值(Non-Maximum Suppression)抑制，以消除边缘检测带来的杂散响应
4.应用双阈值(Double-Threshold)检测来确定真实的和潜在的边缘,maxvalue和minvalue
5.通过抑制孤立的弱边缘最终完成边缘检测
"""

v1=cv2.Canny(img,80,150)    #80是minvalue,150是maxvalue
v2=cv2.Canny(img,50,100)    #50是minvalue,100是maxvalue

res=np.hstack((v1,v2))
cv_show('res',res)





