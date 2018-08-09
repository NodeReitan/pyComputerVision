import numpy as np
import cv2
import video

if __name__ == '__main__':
	# создаем окно cam
	cv2.namedWindow( "cam" )
	cv2.namedWindow( "mz" )
	
	# создаем объект cap для захвата кадров с камеры
	cap = cv2.VideoCapture(0)
	
	while True:
	    # захватываем текущий кадр и кладем его в переменную img 
	    flag, img = cap.read()
	    try:
	        # отражаем кадр
	        img = cv2.flip(img,1)
	
	        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	        gray = cv2.GaussianBlur(gray, (3, 3), 0)
	        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	        edged = cv2.Canny(gray, 10, 250)
	        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

	        # отображаем кадр в окне с именем cam
	        cv2.imshow('cam', (1-gray)*(edged))
	        cv2.imshow('mz', edged)
	        # print (cap.get(cv2.CAP_PROP_FPS))
	    except:
	        cap.release()
	        raise
	
	    ch = cv2.waitKey(5)# esc выход из программы
	    if ch == 27: 
	        break
	
	cap.release()
	cv2.destroyAllWindows()