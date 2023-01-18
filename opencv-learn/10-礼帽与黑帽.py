# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)礼帽运算
cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)黑帽运算
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll5.jpg',cv2.IMREAD_COLOR)
cv_show('img',img)

#礼帽=原始输入-开运算结果
kernel=np.ones((5,5),np.uint8)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv_show('tophat',tophat)

#黑帽=闭运算-原始输入
kernel=np.ones((5,5),np.uint8)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv_show('blackhat',blackhat)
"""
礼帽：取出亮度高的地方
     顶帽运算 = 原图像 - 开运算
     开运算可以消除暗背景下的高亮区域，那么如果用原图减去开运算结果就可以得到原图中灰度较亮的区域，所以又称白顶帽变换。
黑帽：取出亮度低的地方
     底帽运算 = 原图像 - 闭运算
     闭运算可以删除亮背景下的暗区域，那么用原图减去闭运算结果就可以得到原图像中灰度较暗的区域，所以又称黑底帽变换。

"""