import cv2


def part1():
    imj = cv2.imread("C:\AZOM_Labs\lab1\picts\pict.jpeg")
    cv2.imshow("output",imj)
    cv2.waitKey(0)

def part2(wind,color,num):
    img1 = cv2.imread(r'C:\AZOM_Labs\lab1\picts\pict.jpeg',color)
    cv2.namedWindow('Display window'+str(num), wind)
    cv2.imshow('Display window'+str(num), img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def part3(color,size):
    cap = cv2.VideoCapture(r'C:\AZOM_Labs\lab1\picts\video.mp4', cv2.CAP_ANY)

    while True:
        ret, frame = cap.read()
        if not (ret):
            break
        col_frame = cv2.cvtColor(frame,color)
        resize_frame = cv2.resize(col_frame,size)
        cv2.imshow('frame', resize_frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break

def task3():
    a = [cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2HSV, cv2.COLOR_RGB2HLS]
    b = [(640, 480), (500, 500), (430, 430)]
    for i in a:
        for j in b:
            part3(i, j)
def part4():
    video = cv2.VideoCapture("C:/AZOM_Labs/lab1/picts/video.mp4")

    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.mov", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()
        cv2.imshow('img', img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

def part5():
    img1 = cv2.imread(r'C:\AZOM_Labs\lab1\picts\pict.jpeg')
    hsv_img = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)

    cv2.imshow('Original Image', img1)
    cv2.imshow('HSV Image', hsv_img)

    cv2.waitKey(0)


# part1()

# part2(cv2.WINDOW_NORMAL,cv2.IMREAD_COLOR,1)
# part2(cv2.WINDOW_AUTOSIZE,cv2.IMREAD_GRAYSCALE,2)
# part2(cv2.WINDOW_FULLSCREEN,cv2.IMREAD_UNCHANGED,3)

# task3()

part4()