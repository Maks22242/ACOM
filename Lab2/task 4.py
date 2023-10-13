import cv2
import numpy as np

def S(mask,frame):
    # Находим контуры объектов на маске
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Инициализируем переменную для площади
    area = 0

    # Если найдены контуры
    if len(contours) > 0:
        # Выбираем самый большой контур (самый большой объект)
        largest_contour = max(contours, key=cv2.contourArea)

        # Находим моменты первого порядка объекта
        moments = cv2.moments(largest_contour)

        # Вычисляем площадь объекта
        area = moments['m00']

        # Отображаем контур объекта
        cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
        # Отображаем площадь объекта на экране
    # cv2.putText(frame, f'Area: {area}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame



def task7():
    w = 640
    h = 480
    cap = cv2.VideoCapture(0)
    cap.set(3,w)
    cap.set(4,h)
    # Определяем диапазон красного цвета в HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])


    while True:
        ret, frame = cap.read()
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Создаем маску для красного цвета
        mask = cv2.inRange(hsv_img, lower_red, upper_red)
        # result = cv2.bitwise_and(frame, frame, mask=mask)
        # Морфологическое открытие (erosion followed by dilation)
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


        # Морфологическое закрытие (dilation followed by erosion)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        areaObject = S(closing,frame)

        cv2.imshow('result', areaObject)
        cv2.imshow('mask', mask)
        cv2.imshow('op', opening)
        cv2.imshow('clos', closing)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

task7()