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
img=cv2.imread(r'D:\OpenCvLearning\lll.jpg',cv2.IMREAD_COLOR)

#设置边框延伸大小
top_size,bottom_size,left_size,right_size=(100,100,100,100)
#设置常用参数
replicate=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_CONSTANT,value=100)
'''其中constant方法中若要改变边框颜色可以改变value的值'''

#展示不同模式的效果
plt.subplot(231),plt.imshow(img,'gray'),plt.title ('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT 101')
plt.subplot(235),plt.imshow (wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow (constant,'gray'),plt.title('CONSTANT')
'''
BORDER_REPLICATE:复制法，复制最边缘像素
BORDER_REFLECT:反射法，对感兴趣图像中的像素在两边进行复制，例如:fedcba|abcdefgh|hgfedcb
BORDER_REFLECT_101:反射法，也就是以最边缘像素为轴对称，例如:gfedcb|abcdefgh|gfedcba
BORDER_WRAP:外包装法，例如:cdefgh|abcdefgh|abcdefg
BORDER_CONSTANT:常量法，常数值填充
'''
plt.show()  #展示matplot绘图




