# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)灰度化
cv2.threshold(gray,127,255,cv2.THRESH_BINARY)图像阈值化处理
contours,binary=cv2.findContours(img,mode,method)注意这个函数有两个返回值
cv2.drawContours(draw_img,contours,-1,(0,0,255),2)绘制轮廓
cv2.contourArea(cnt_out)获取特定轮廓的面积
cv2.arcLength(cnt_out,True)获取特定轮廓的周长
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll8.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

"""
函数原型:cv2.findContours(img,mode,method)
mode:轮廓检索模式
    RETR_EXTERNAL(也很常用):只检索最外面的轮廓
    RETR_LIST:检索所有的轮廓,并将其保存到一条链表中
    RETR_CCOMP:检索所有轮廓，并将他们组织为两层:顶层是各部分的外部边界，第二层是空洞的边界
    RETR_TREE(最常用):检索所有的轮廓,并重构嵌套轮廓的整个层次
method:轮廓逼近方法
    CHAIN_APPROX_NONE:以Freeman链码的方式输出轮廓,所有其他方法输出多边形
    CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分，也就是函数只保留他们的终点部分
为了更高的准确率,常常使用二值图像
"""

#必须先用二值检测，才可以用检测操作
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv_show('thresh',thresh)

#边缘检测
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#绘制轮廓,传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
"""人像绘制"""
draw_img=img.copy() #注意必须要copy,不然原图会变
res=cv2.drawContours(draw_img,contours,-1,(0,0,255),2)  #-1默认为画所有轮廓,BGR(0,0,255)
cv_show('res',res)

"""
cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
    -1是默认画所有图像,0是按顺序第一个图像的外轮廓,1是按顺序第一个图像的内轮廓,以此类推
    (0,0,255)是BGR，控制线条颜色
    2是线条宽度
"""

"""常见图形的绘制"""
img1=cv2.imread(r'D:\OpenCvLearning\lll9.jpg') #注意必须要copy,不然原图会变
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
draw_img1=img1.copy()
contours1,hierarchy1=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
res1=cv2.drawContours(draw_img1,contours1,0,(0,0,255),2)
cv_show('res1',res1)

#轮廓特征(面积,周长等)
for i in range(4):
    cnt_out=contours1[2*i]
    cnt_in=contours1[2*i+1]
    area_out = cv2.contourArea(cnt_out)  #外轮廓面积
    area_in = cv2.contourArea(cnt_in)  #内轮廓面积
    length_out = cv2.arcLength(cnt_out,True)  #外轮廓哟周长,True表示闭合的
    length_in = cv2.arcLength(cnt_in,True)  #内轮廓周长,True表示闭合的
    print("第",i+1,"个图形的外轮廓")
    print("area:", area_out)
    print("length:", length_out)
    print("第",i+1,"个图形的内轮廓")
    print("area:",area_in)
    print("length:",length_in)
