# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
cv2.Scharr(img,cv2.CV_64F,1,0)
cv2.Laplacian(img,cv2.CV_64F)
cv2.convertScaleAbs(sobely)
cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll6.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(500,500))
cv_show('img',img)

""" 
scharr算子比sobel更加敏感一点
lapalacian算子对噪音点比较敏感，在使用时效果不是特别好，因此通常与别的算子相结合
"""

#不同算子的差异
"""sobel算子"""
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely=cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

"""scharr算子"""
scharrx=cv2.Scharr(img,cv2.CV_64F,1,0)
scharrx=cv2.convertScaleAbs(sobelx)
scharry=cv2.Scharr(img,cv2.CV_64F,0,1)
scharry=cv2.convertScaleAbs(sobely)
scharrxy=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

"""laplacian算子"""
laplacian=cv2.Laplacian(img,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)

res=np.hstack((sobelxy,scharrxy,laplacian))
cv_show('res',res)
