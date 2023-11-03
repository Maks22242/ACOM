import cv2
import numpy as np


def tracking():
    cap = cv2.VideoCapture(r'C:\AZOM_Labs\lab5\moves\ЛР4_main_video.mov', cv2.CAP_ANY)
    #Проверка на первый кадр
    start_tracking = True
    oldImage = 0

    # Определяем параметры для операции двоичного разделения
    threshold_value = 30
    max_binary_value = 255
    binary_threshold = cv2.THRESH_BINARY

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("mymov.mov", fourcc, 25, (w, h))

    while True:
        ret, frame = cap.read()
        if not (ret):
            break
        # Переводим в чёрнобелый цвет
        image =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Применяем размытие по Гаусу
        blurred_image = cv2.GaussianBlur(image, (5, 5), 3)
        if start_tracking:
            start_tracking = False
            oldImage = blurred_image
        else:
            destination_image = cv2.absdiff(image, oldImage)
            _, thresholded = cv2.threshold(destination_image, threshold_value, max_binary_value, binary_threshold)

            # Находим контуры объектов
            contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Проходим по контурам и находим контур с заданной площадью
            min_contour_area = 1000  # Задайте своё значение
            for contour in contours:
                if cv2.contourArea(contour) > min_contour_area:
                    # Записываем кадр с движением в файл
                    video_writer.write(frame)
                    print("save")
            # Отобразим видео
        cv2.imshow('Video', frame)

        if cv2.waitKey(30) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


tracking()
