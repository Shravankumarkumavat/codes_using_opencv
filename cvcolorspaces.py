import cv2 as cv


img=cv.imread('ataksuki.jpg')
cv.imshow('img',img)


# BGR(blue,green,red) to grayscale
# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

#BGR to hsv
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)


#bgr to lab
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('lab',lab)

#bgr to rgb
# rgb = cv.cvtColor(img,cv.COLOR_BGRA2RGB)
# cv.imshow('rgb',rgb)

# grayslace to hsv [ gray to bgr to hsv( direct is not possible  and same for gray to lab)
# hsv_bgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('hsv to bgr',hsv_bgr)
# bgr_gray= cv.cvtColor(hsv_bgr, cv.COLOR_BGR2GRAY)
# cv.imshow('bgr to gray',bgr_gray)














cv.waitKey(0)