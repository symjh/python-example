import numpy as np
import cv2

url = "2.jpg"
# 载入图片 img是每一个像素点的BGR颜色 格式是Numpy的?
img = cv2.imread(url)
# x 100 y 100 点的BGR颜色
px=img[100,100]
# x 100 y 100 点的B的值
blue=img[100,100,0]
# 修改某一像素点的值
img[100,100]=[255,255,255]

# 行数，列数，通道数的元组
print(img.shape)
# 图像的数据类型  img.dtype 非常重要。因为在 OpenCV Python 代码中经常出现数据类型的不一致。
print(img.size, img.dtype)



# 截取图片中的月亮 100 40 330 260
# y轴在前 x轴在后??
moon = img[40:260,100:330]
# 复制月亮至 (460,40) (690,260)
img[40:260,460:690] = moon

# 显示图片
cv2.imshow('test', img)

# 等待，不让程序结束
cv2.waitKey(0)
