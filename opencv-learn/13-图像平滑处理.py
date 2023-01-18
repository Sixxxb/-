# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.blur(img,(3,3))
cv2.boxFilter(img,-1,(3,3),normalize=True)
cv2.GaussianBlur(img,(5,5),1)
cv2.medianBlur(img,5)
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll8.jpg',cv2.IMREAD_COLOR)
cv_show('img',img)

#均值滤波(简单的平均卷积操作)
blur=cv2.blur(img,(3,3))
cv_show('blur',blur)

#方框滤波(基本和均值一样,可以选择归一化)
box=cv2.boxFilter(img,-1,(3,3),normalize=True)  #normalize是归一化的意思，必须要True
cv_show('box',box)

#高斯滤波(高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的)
gaussian=cv2.GaussianBlur(img,(5,5),1)
cv_show('gaussian',gaussian)

#中值滤波(相当于用中值代替)
median=cv2.medianBlur(img,5)
cv_show('median',median)

res=np.hstack((blur,gaussian,median))
print(res)
cv_show('blur,gaussian,median',res)
