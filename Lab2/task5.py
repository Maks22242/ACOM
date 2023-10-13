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
        if area > 0:
            frame = createBlackSquare(frame,area,moments,largest_contour)

        return frame

def createBlackSquare(frame,area,moments,largest_contour):
    #Сумма значений пикселей, умноженных на их колординаты
    center_x = int(moments['m10'] / area)
    center_y = int(moments['m01'] / area)

    # Рисуем черный прямоугольник вокруг объекта
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
    # Отображаем результаты, включая центр объекта
    # cv2.putText(frame, f'Area: {area}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
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

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

task7()