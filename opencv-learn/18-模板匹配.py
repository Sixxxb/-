# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
'''函数合集
cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)图像匹配程度
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)图像匹配的最小值，最大值，最小值坐标，最大值坐标
cv2.rectangle(img2,top_left,bottom_right,255,2)画矩形
np.where(res>=threshold)返回满足条件的坐标
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread('D:\OpenCvLearning\lll8.jpg',0)
template=cv2.imread('D:\OpenCvLearning\lll14.jpg',0)
h,w=template.shape[:2]  #除了第三位的3其他两位表示图像的大小
"""
cv2.COLOR_BGR2GRAY相当于0，是一个宏替换
cv2.IMREAD_COLOR相当于1，是一个宏替换
"""

methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR',
        'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
"""
TM_SQDIFF(0)：计算平方不同，计算出来的值越小，越相关
TM_CCORR(2)：计算相关性，计算出来的值越大，越相关
TM_CCOEFF(4)：计算相关系数，计算出来的值越大，越相关
TM_SQDIFF_NORMED(1)：计算归一化平方不同，计算出来的值越接近0，越相关
TM_CCOEFF_NORMED(5)：计算归一化相关系数，计算出来的值越接近1，越相关
"""
res=cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
print(res.shape)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
print(min_val,max_val,min_loc,max_loc)

for meth in methods:
    img2=img.copy()

    #匹配方法的真值
    method=eval(meth)   #eval是将字符串转为相对应的值(解开宏定义)
    print(method)
    res=cv2.matchTemplate(img,template,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    """
        min_loc和max_loc均为一个坐标(元组),因此在后面会有如top_left[0],
    top_left[1]此类的用法
    """

    #如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED,取最小值
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    bottom_right=(top_left[0]+w,top_left[1]+h)

    #画矩形
    cv2.rectangle(img2,top_left,bottom_right,(0,0,255),2)

    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img2,cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.suptitle(meth)
    plt.show()

#匹配多个对象
img_rgb=cv2.imread(r'D:\OpenCvLearning\lll16.jpg')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template=cv2.imread(r'D:\OpenCvLearning\lll15.jpg',0)
h,w=template.shape[:2]

res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)#越接近1越相关
threshold=0.5   #设定阈值，取匹配程度大于%70的坐标
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):  #*表示可选参数
    bottom_right=(pt[0]+w,pt[1]+h)
    cv2.rectangle(img_rgb,pt,bottom_right,(0,0,255),2)

cv_show('img_rgb',img_rgb)

