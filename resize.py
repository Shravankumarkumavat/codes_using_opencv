import cv2 as cv


#for image , video and live video
def rescaleframe(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions, interpolation=cv.INTER_AREA)


#for live video only
def changeresolution(width, height):
    capture.set(3,width)
    capture.set(4,height)


cap = cv.VideoCapture(0)
while True :
    inTrue, frame = cap.read()
    
    frame_resize = rescaleframe(frame)

    cv.imshow('video',frame)
    cv.imshow('video resized', frame_resize)


    if cv.waitKey(25) & 0xFF == ord('q'):

        break

cap.release()
cv.destroyAllWindows()




img = cv.imread('ataksuki.jpg')
cv.imshow('image',img)
resize_img  = rescaleframe(img)
cv.imshow('image resized', resize_img)
cv.waitKey(0)