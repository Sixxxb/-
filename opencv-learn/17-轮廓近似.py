# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(draw_img,contours[0],-1,(0,0,255),2)
epsilon=0.05*cv2.arcLength(cnt,True)设定误差值
cv2.approxPolyDP(cnt,epsilon,True)获得近似轮廓
x,y,w,h=cv2.boundingRect(cnt)轮廓的外接矩形四个点的认定
cv2.rectangle(draw_img,(x,y),(x+w,y+h),(0,255,0),2)获得轮廓的外界矩形
(x,y),radius=cv2.minEnclosingCircle(cnt)轮廓的外接圆的坐标和半径
cv2.circle(img,center,radius,(255,0,0),2)画圆，在这里是画出相对应的外接圆
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll10.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt=contours[0] #找到其中的一个轮廓

#画出原轮廓
draw_img=img.copy()
res=cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)
cv_show('res',res)

#设定近似的轮廓
epsilon=0.05*cv2.arcLength(cnt,True)    #epsilon误差(阈值)
approx=cv2.approxPolyDP(cnt,epsilon,True)   #approx近似后的轮廓
"""
epsilon的值越小，近似就越少，跟原轮廓偏差越小
epsilon的值越大，近似就越多，跟原轮廓偏差越大
approx实际上也是一个“contours”,是一个轮廓，但是是近似后的
"""

#显示近似后的轮廓
draw_img=img.copy()
res=cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)
cv_show('res',res)

#画出轮廓的外接矩形
x,y,w,h=cv2.boundingRect(cnt)
img=cv2.rectangle(draw_img,(x,y),(x+w,y+h),(0,255,0),2)
cv_show('rect',img)

#计算轮廓面积和外界矩形面积的比值
area=cv2.contourArea(cnt)
x,y,w,h=cv2.boundingRect(cnt)
rect_area=w*h
extent=float(area)/rect_area
print("轮廓面积与边界矩形比:",extent)

#外接圆
(x,y),radius=cv2.minEnclosingCircle(cnt)
center=(int(x),int(y))
radius=int(radius)
img=cv2.circle(img,center,radius,(255,0,0),2)
cv_show('circle',img)
