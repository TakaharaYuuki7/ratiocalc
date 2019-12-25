#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# 閾値
threshold_value = 127

# 入力画像の読み込み
img = cv2.imread("sem.jpg")

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 出力画像用の配列生成
threshold_img = gray.copy()

# NumPyで実装
threshold_img[gray < threshold_value] = 0
threshold_img[gray >= threshold_value] = 255

# 結果を出力
cv2.imwrite("example.png", threshold_img)

#ヒストグラム作成
#先ほど作成した白黒ファイルを読み込む
img = cv2.imread('example.png')
color = ('b')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

#白と黒の値をそれぞれ表示
yb = sum(histr[0])
print("黒：" + str(yb))

yw = sum(histr[255])
print("白：" + str(yw))

#割合を算出
per_yb = yb * 100 / (yb + yw)
per_yw = yw * 100 / (yb + yw)

print('白は{:.4f}%です。'.format(per_yw))
print("黒は{:.4f}%%です。".format(per_yb))

#画像表示
im = Image.open("example.png")

im.show()
plt.show()
