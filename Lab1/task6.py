import cv2

def draw_a_frames(img, width,height,rect_width1,rect_height1,rect_width2,rect_height2):
    # height, width,  = img.shape

    top_left_x = (width - rect_width1) // 2
    top_left_y = (height - rect_height1) // 2
    bottom_right_x = top_left_x + rect_width1
    bottom_right_y = top_left_y + rect_height1
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)



    top_left_x = (width - rect_width2) // 2
    top_left_y = (height - rect_height2) // 2
    bottom_right_x = top_left_x + rect_width2
    bottom_right_y = top_left_y + rect_height2
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)
    ROI = img[top_left_y:top_left_y + rect_height2, top_left_x:top_left_x + rect_width2]
    blur = cv2.GaussianBlur(ROI, (101, 1), 30)
    img[top_left_y:top_left_y + rect_height2, top_left_x:top_left_x + rect_width2] = blur
    return img

def print_cam(height,width):
    cap = cv2.VideoCapture(0)
    cap.set(3,height)
    cap.set(4,width)
    while True:
        ret, frame = cap.read()
        reFrame = draw_a_frames(frame,height,width,100,300,300,100)

    # Display the resulting frame
        cv2.imshow('frame', reFrame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

print_cam(1040,480)