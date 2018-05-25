import cv2
import numpy as np

def calledFunction():
    pass

def main():
    imgArr = np.zeros((512,512,3),np.uint8)
    winName = 'OpenCV Colour Palette'
    cv2.namedWindow(winName)
    
    cv2.createTrackbar('Blue',winName,0,255,calledFunction)
    cv2.createTrackbar('Green',winName,0,255,calledFunction)
    cv2.createTrackbar('Red',winName,0,255,calledFunction)
    
    while(True):
        cv2.imshow(winName,imgArr)
        if cv2.waitKey(1) == 27:
            break
        Blue = cv2.getTrackbarPos('Blue',winName)
        Green = cv2.getTrackbarPos('Green',winName)
        Red = cv2.getTrackbarPos('Red',winName)
        
        imgArr[:]=[Blue,Green,Red]
        
    cv2.destroyAllWindows()
    

main()