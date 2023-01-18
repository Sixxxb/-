# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
cv2.IMREAD_COLOR指读取彩色图像
cv2.IMREAD_GRAYSCALE指读取灰度图像
但是默认读取彩色图
'''
'''函数汇总
cv2.imread(r'路径名',灰度/彩色)
cv2.imshow(’创建的播放窗口名‘，对象名)
cv2.waitKey(num)
cv2.destroyAllWindows()
'''
#imread函数中不可以有中文路径，并且一定要加r取消转义字符！！
#不然反斜杠会被识别为转义字符而导致路径错误
img1=cv2.imread('D:\OpenCvLearning\lll.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('D:\OpenCvLearning\lll.jpg',cv2.IMREAD_GRAYSCALE)
print(img1)  #输出读取的图片，化为矩阵的形式
print(img1.shape)  #输出图片的大小  第三个数字是3，意思是RGB
print(img1.dtype)  #输出图片的类型
print(img1.max())  #输出图片的最大值
print(img1.min())  #输出图片的最小值

#图像的显示
cv2.imshow('img1',img1) #第一个参数是显示图片窗口的名称
print("按下任何按键即可退出，并且显示灰度图像")
cv2.waitKey(0)  #按下任何按键退出
    #如果是cv2.waitKey(x)就是窗口显示（x/1000）秒后关闭
cv2.destroyAllWindows()
#此处可以令上面三个函数集成于一个函数
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cv_show('img2',img2)

#图像的保存
cv2.imwrite(r'C:\Users\think book\Desktop\lll2.jpg',img2)

