import cv2 as cv
import numpy as np



img= cv.imread('ataksuki.jpg')
cv.imshow('img',img)

# def transfrom(img, x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions= (img.shape[1],img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)


# shifted= transfrom(img,-100,-100)
# cv.imshow('shifted',shifted)



# def rotate( img , angle , rotpoint=None):
#     (height,width) =img.shape[:2]
#     if rotpoint is None:
#         rotpoint = (width//2,height//2)
#     rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
#     dimensions =(width,height)
#     return cv.warpAffine(img,rotMat, dimensions)

# rotated = rotate(img,-45)
# cv.imshow('rotated',rotated)

flip =cv.flip(img,-1) # 0,1,-1
cv.imshow('flipped',flip)






cv.waitKey(0)