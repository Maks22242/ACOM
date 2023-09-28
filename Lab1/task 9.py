import cv2
video = cv2.VideoCapture("http://192.168.43.1:8080/video")
ok, img = video.read()
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter("outputcamtel.mov", fourcc, 25, (w, h))
while (True):
    ok, img = video.read()
    cv2.imshow('img', img)
    video_writer.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()