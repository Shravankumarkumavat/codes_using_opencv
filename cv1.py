import cv2 as cv 
#img = cv.imread('ataksuki.jpg')
#cv.imshow('redmoon',img)
#cv.waitKey(0)




cap = cv.VideoCapture('C:\dataset\videocaption\video_200-20230211T145621Z-001\video_200\2F9jX7u5nOg_83_97.avi')

while True:
    isTrue, frame = cap.read() 
    cv.imshow('Video', frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()






