# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''
    视频处理实际上是对每一帧的图像进行处理，也就是说读取视频的过程实际上就是
读取图像的过程，在此处需要使用cv2.VideoCapture(namepath)函数，参数是图像路径
'''
cap = cv2.VideoCapture(r'D:\OpenCvLearning\2022.9.MOV') #读取视频文件
#使用.isOpened()函数来判断视频是否被读取了
if cap.isOpened():  #判断视频是否被读取，并且指定对象为cap，cap可更改为任意名字
    open,frame=cap.read()   #cap.read()即为读取cap对象内的视频，并赋值给frame
else:
    open=False

while(open):
    ret, frame = cap.read()
    if ret == True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #将视频处理为灰色
        cv2.imshow('frame', gray)
        if cv2.waitKey(10) & 0xFF == ord('q'):  #按下q结束进程
            break
cap.release()
cv2.destroyAllWindows()
