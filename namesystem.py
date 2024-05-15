import cv2

img = cv2.imread("C:/Users/This PC/Desktop/Python/projects/104/solar-system.jpg")
cv2.putText(img,"Sun",(100,100),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img,"Mercury",(110,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Venus",(190,270),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Earth",(290,270),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Mars",(380,270),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Jupiter",(420,130),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Saturn",(820,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Uranus",(950,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.51,color=(0,0,255))
cv2.putText(img,"Neptune",(1100,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.51,color=(0,0,255))
cv2.imshow("solar",img)
cv2.waitKey(0)