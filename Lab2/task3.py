import cv2
import numpy as np


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

        cv2.imshow('mask', mask)
        cv2.imshow('frame', frame)
        cv2.imshow('hsv', hsv_img)
        cv2.imshow("op", opening)
        cv2.imshow("clos",closing)
        # cv2.imshow('result', result)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

task7()