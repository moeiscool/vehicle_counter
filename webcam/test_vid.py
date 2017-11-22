import cv2
import numpy as np

cam = cv2.VideoCapture("../vid/recording_8s.mp4")
back_sub = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((5,5),np.uint8)
learningRate = 0.1

while True:
    ret, image = cam.read()

    gray = np.float32(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY))
    foreground = back_sub.apply(gray, None, learningRate)
    #erosion followed by dilation (useful for removing noise around foreground obj)
    opening = cv2.morphologyEx(foreground, cv2.MORPH_OPEN, kernel) 

    cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original", 600,600)
    cv2.imshow("Original",image)

##    cv2.namedWindow("Foreground",cv2.WINDOW_NORMAL)
##    cv2.resizeWindow("Foreground", 600,600)
##    cv2.imshow("Foreground",foreground)
    
    cv2.namedWindow("Opening",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Opening", 600,600)
    cv2.imshow("Opening", opening)
    
    """
    #shows corners
    copy = image.copy()
    gray = np.float32(cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY))
    corners = cv2.dilate(cv2.cornerHarris(gray,2,3,0.04),None)
    copy[corners>0.02*corners.max()]=[0,0,255]
    cv2.imshow("Corners",copy)
    """
    """
    #erodes away the boundaries of foreground objects
    erosion = cv2.erode(image,kernel,iterations = 1)
    cv2.imshow("Erosion", erosion)
    """
    """
    #increases size of foreground objects
    dilation = cv2.dilate(image,kernel,iterations = 1)
    cv2.imshow("Dilation", dilation)
    """
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
