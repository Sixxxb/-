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

img =cv2.imread(r'D:\OpenCvLearning\lll.jpg',cv2.IMREAD_COLOR)
part =img[200:600,400:600]
cv_show('img',part)

#颜色通道提取（分离颜色通道）
b,g,r=cv2.split(img)
print(r.shape)
print(g.shape)
print(b.shape)
cv_show('b',b)
cv_show('g',g)
cv_show('r',r)

#合并颜色通道
img_merge=cv2.merge([b,g,r])    #.merge是合并颜色通道的函数方法
cv_show('merge',img_merge)
print(img_merge.shape)

#只保留个别颜色通道
'''只保留R'''
cur_img=img.copy()
cur_img[:,:,0]=0
cur_img[:,:,1]=0
cv_show('only R',cur_img)

'''只保留G'''
cur_img=img.copy()
cur_img[:,:,0]=0
cur_img[:,:,2]=0
cv_show('only G',cur_img)

'''只保留B'''
cur_img=img.copy()
cur_img[:,:,1]=0
cur_img[:,:,2]=0
cv_show('only B',cur_img)
