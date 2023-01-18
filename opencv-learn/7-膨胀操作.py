# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数汇总
cv2.erode(img,kernel,iterations=2)
cv2.dilate(img_erosion,kernel,iterations=2)
np.hstack((img_dilate_1,img_dilate_2,img_dilate_3))
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll4.jpg',cv2.IMREAD_COLOR)
cv_show('img',img)

#腐蚀操作
kernel=np.ones((8,8),np.uint8)
img_erosion=cv2.erode(img,kernel,iterations=5)
cv_show('img_erosion',img_erosion)

#膨胀操作
kernel=np.ones((12,12),np.uint8)
img_dilate=cv2.dilate(img_erosion,kernel,iterations=2)
cv_show('img_dilate',img_dilate)

img_dilate_1=cv2.dilate(img_erosion,kernel,iterations=3)
img_dilate_2=cv2.dilate(img_erosion,kernel,iterations=6)
img_dilate_3=cv2.dilate(img_erosion,kernel,iterations=9)
res=np.hstack((img_dilate_1,img_dilate_2,img_dilate_3))
cv_show('res',res)