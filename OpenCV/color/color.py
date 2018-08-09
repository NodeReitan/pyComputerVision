#	https://arboook.com/kompyuternoe-zrenie/operatsii-s-tsvetom-v-opencv3-i-python/
import cv2

image = cv2.imread("1-1.jpg")#	загрузка изображения
#cv2.imread возвращает NumPy массив, который содержит представление данных из изображения.

#---------------------------------------------------------------------------#
# как выглядят слои
#cv2.imshow('Color blue',image[:,:,0])
#cv2.imshow('Color green',image[:,:,1])
#cv2.imshow('Color red',image[:,:,2])
#---------------------------------------------------------------------------#
# в cv2 система BGR, а не RGB!!!	<---------
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)#что будет, если перепутоть
#---------------------------------------------------------------------------#
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_GRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_LAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
image_XYZ = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
image_YUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
#---------------------------------------------------------------------------#

cv2.imshow("Original image", image)# вывод изображения
cv2.waitKey(0)# ждём нажатия клавиши