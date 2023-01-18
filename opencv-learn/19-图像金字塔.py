# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll15.jpg',1)
print(img.shape)
cv_show('img',img)
"""采样方法
高斯金字塔：向下采样方法（缩小）
高斯金字塔：向上采样方法（放大）
拉普拉斯金字塔
"""
#高斯金字塔
up=cv2.pyrUp(img)
cv_show('up',up)
print(up.shape)

down=cv2.pyrDown(img)
cv_show('down',down)
print(down.shape)

up2=cv2.pyrUp(up)
cv_show('up2',up2)
print(up2.shape)

down2=cv2.pyrDown(down)
cv_show('down2',down2)
print(down2.shape)

up=cv2.pyrUp(img)   #先上采样再下采样后，效果会比原图要差
up_down=cv2.pyrDown(up)
res=np.hstack((img,up_down))
cv_show('up_down',res)

#拉普拉斯金字塔
down=cv2.pyrDown(img)
down_up=cv2.pyrUp(down)
print(img.shape)
down_up=cv2.resize(down_up,(375,386))
l_l=img-down_up
cv_show('l_l',l_l)
