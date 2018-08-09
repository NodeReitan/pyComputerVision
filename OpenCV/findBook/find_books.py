import numpy as np
import cv2

# загрузите изображение, смените цвет на оттенки серого и уменьшите резкость
image = cv2.imread("2-1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("gray.jpg", gray)

#распознание контуров
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("edged.jpg", edged)

#создайте и примените закрытие (заливка белым)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closed.jpg", closed)

# найдите контуры в изображении и подсчитайте количество книг
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
total = 0

for c in cnts:
    # аппроксимируем (сглаживаем) контур
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # если у контура 4 вершины, предполагаем, что это книга
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1

#вывод изображения на экран
cv2.imshow("Original image", image)
print("Я нашёл {0} книг на этой картинке".format(total))
cv2.waitKey(0)