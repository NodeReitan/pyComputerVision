#	https://arboook.com/kompyuternoe-zrenie/nahodim-tsvetnoj-predmet-v-kadre-s-pomoshhyu-opencv-3-python/
import cv2
import numpy as np

image = cv2.imread('1-1.jpg')
#---------------------------------------------------------------------------#
# ищем рыжого кота на зелёном фоне
low_red = (17,50,110)
high_red = (101,140,180)
# в итоге мы получили куб цветов, куда кроме нужных цветов попала куча фигни
only_cat = cv2.inRange(image, low_red, high_red)
# много шума, не весь цветовой диапозон
#---------------------------------------------------------------------------#
# исправляем ошибки первого варианта
# описание сие действия очень громозко см источник
cat_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Преобразуем в HSV
cat_color_low = (7,40,60) #Данный цвет это темный ненасыщенный красный, близкий к бордовому
cat_color_high = (18,255,200) #Данный цвет это светлый насыщенный оранджевый
only_cat_hsv = cv2.inRange(cat_hsv, cat_color_low, cat_color_high)
# теперь мы видим лапы и хвост)
#---------------------------------------------------------------------------#
moments = cv2.moments(only_cat_hsv, 1) # получим моменты 
x_moment = moments['m01']
y_moment = moments['m10']
area = moments['m00']
x = int(x_moment / area) # Получим координаты x,y кота
y = int(y_moment / area) # и выведем текст на изображение
cv2.putText(image, "Cat!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) 
#---------------------------------------------------------------------------#
cv2.imshow('only car', image)
cv2.waitKey(0)