# 欢迎来到刘b的python之路！
# 在这里开始你的电赛飞控之旅！
# 祝你好运 终会抵达
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
"""函数合集
cv2.resize(img,(500,500))重置图像的大小
cv2.add(img,img1)将图片的对应参数相加
cv2.addWeighted(img1,0.4,img2,0.6,0)将图像像按比例叠加
"""
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图片
img=cv2.imread(r'D:\OpenCvLearning\lll.jpg',cv2.IMREAD_COLOR)

img1=img+10 #img的所有位置都加了10
print("img\n",img[:5,:,0])    #最后一个参数只能为0(B),1(G),2(R)
print("img\n",img1[:5,:,0])
print("img+img1\n",(img+img1)[:5,:,0])    #相当于每个数对256求余

print("add(img,img1)\n",cv2.add(img,img1)[:5,:,0])    #在cv2里的add加法，如果越界，则统一显示255

#图像融合--实现两张图片按比例的融合
img2=cv2.imread(r'D:\OpenCvLearning\lll3.jpg',cv2.IMREAD_COLOR)
print("img1:",img1.shape)
print("img2:",img2.shape)
if img1.shape==img2.shape:
    print("两张图片大小相同")
else:
    print("两张图片大小不相同")
    img1=cv2.resize(img,(img2.shape[1],img2.shape[0]))  #注意要反着取，不然会颠倒
    print("img1:", img1.shape)
    print("img2:", img2.shape)

#图像融合
res1=cv2.addWeighted(img1,0.4,img2,0.6,0)    #img1是重新设置后的图像而img不是，因此img和img2不能相加
res2=cv2.addWeighted(img1,0.2,img2,0.8,0)    #img1是重新设置后的图像而img不是，因此img和img2不能相加
res3=cv2.addWeighted(img1,0.5,img2,0.5,0)    #img1是重新设置后的图像而img不是，因此img和img2不能相加
plt.subplot(231),plt.imshow(res1),plt.title('4:6')
plt.subplot(232),plt.imshow(res2),plt.title('2:8')
plt.subplot(233),plt.imshow(res3),plt.title('5:5')
plt.show()

#图像大小、比例的修改
res1=cv2.resize(img,(0,0),fx=1,fy=1)
res2=cv2.resize(img,(0,0),fx=4,fy=4)
res3=cv2.resize(img,(0,0),fx=2,fy=1)
res4=cv2.resize(img,(400,400))
res5=cv2.resize(img,(100,400))
res6=cv2.resize(img,(200,100))

plt.subplot(231),plt.imshow(res1),plt.title('1:1')
plt.subplot(232),plt.imshow(res2),plt.title('4:4')
plt.subplot(233),plt.imshow(res3),plt.title('2:1')
plt.subplot(234),plt.imshow(res4),plt.title('400,400')
plt.subplot(235),plt.imshow(res5),plt.title('100,400')
plt.subplot(236),plt.imshow(res6),plt.title('200,200')
plt.show()



