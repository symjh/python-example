import numpy as np
import cv2

# hsv判断图片颜色好使

url = "2.jpg"
frame = cv2.imread(url)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# 怎么知道hsv的颜色范围 调用
# 这个方法意义不大，因为要找的是区间 请看hsv对照图
rgb_green = np.uint8([[[127,255,0]]])
hsv_green = cv2.cvtColor(rgb_green, cv2.COLOR_BGR2HSV)
print(hsv_green)

# 定义蓝色的范围
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


lower_green = np.array([35,43,46])
upper_green = np.array([77,255,255])

# 掩膜（mask） 就是将低于lower_red和高于upper_red的部分分别变成0 (变成白色) ，lower_red～upper_red之间的值变成255 (变成黑色)
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# cv2.bitwise_and()是对二进制数据进行“与”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“与”操作，1&1=1，1&0=0，0&1=0，0&0=0
# 利用掩膜（mask）进行“与”操作，即掩膜图像白色区域是对需要处理图像像素的保留，黑色区域是对需要处理图像像素的剔除，其余按位操作原理类似只是效果不而已。
res = cv2.bitwise_and(frame,frame, mask= mask)

# 那么用人话说就是 mask 取出这个颜色区间内的像素点
# res 用与运算 算出mask上还存在的像素点 剔除其他像素点

cv2.imshow('green',cv2.bitwise_and(frame,frame, mask= cv2.inRange(hsv,lower_green,upper_green)))

# cv2.imshow('frame',frame)
# cv2.imshow('mask',mask)
# cv2.imshow('res',res)

cv2.waitKey(0)