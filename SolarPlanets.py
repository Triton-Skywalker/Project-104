import cv2

img = cv2.imread('solar-system.jpg')

#Names of Planerts and Sun
cv2.putText(img,'Sun',(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Mercury',(123,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Venus',(195,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Earth',(290,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Mars',(385,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Jupiter',(575,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Saturn',(765,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Uranus',(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Neptune',(1115,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow('Output',img)
cv2.waitKey(0)

cv2.imwrite("NamedSolarSystem.jpg",img)

