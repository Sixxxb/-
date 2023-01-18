# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
np.ones((10,10),np.uint8)设置核的大小
cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)开运算
cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)闭运算
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll5.jpg',cv2.IMREAD_COLOR)
cv_show('img',img)

#开运算：先腐蚀，再膨胀
kernel=np.ones((5,5),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv_show('opening',opening)

#闭运算：先膨胀，再腐蚀
kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv_show('closing',closing)

"""
1.开运算：先对图像腐蚀后膨胀
作用：用来消除小的物体，平滑形状边界，并且不改变其面积。可以去除小颗粒噪声，断开物体之间的粘连。
2.闭运算：先对图像膨胀后腐蚀
作用：用来填充物体内的小空洞，连接邻近的物体，连接断开的轮廓线，平滑其边界的同时不改变面积。
"""