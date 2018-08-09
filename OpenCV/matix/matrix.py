#	https://arboook.com/kompyuternoe-zrenie/osnovnye-operatsii-s-izobrazheniyami-v-opencv-3-python/
import cv2

image = cv2.imread("1-1.jpg")#	загрузка изображения
#cv2.imread возвращает NumPy массив, который содержит представление данных из изображения.

# Нам надо сохранить соотношение сторон
# чтобы изображение не исказилось при уменьшении
# для этого считаем коэф. уменьшения стороны
final_wide = 200
r = float(final_wide) / image.shape[1]
dim = (final_wide, int(image.shape[0] * r))
#---------------------------------------------------------------------------#
# уменьшаем изображение до подготовленных размеров
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#---------------------------------------------------------------------------#
# вырежем участок изображения используя срезы
# мы же используем NumPy
cropped = image[30:130, 150:300]
#---------------------------------------------------------------------------#
# получим размеры изображения для поворота
# и вычислим центр изображения
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
 
# повернем изображение на 180 градусов
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#---------------------------------------------------------------------------#
#отразим изображение по горизонтали
flip_image = cv2.flip(image,1) # 0 – по вертикали, 1 – по горизонтали, (-1) – по вертикали и по горизонтали
#---------------------------------------------------------------------------#
# запишем изображение на диск в формате png
cv2.imwrite("save.png", flip_image)
#---------------------------------------------------------------------------#

cv2.imshow("Original image", flip_image)# вывод изображения
cv2.waitKey(0)# ждём нажатия клавиши