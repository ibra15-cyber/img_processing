import cv2 as cv 
import numpy as np 

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)

circle  = cv.circle(blank.copy(), (200, 200) ,(200), 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise AND ---> insecting regions
bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow("Bitwise AND", bitwise_and)

# bitwise OR non intersecting and intersecting 
bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow("Bitwise or", bitwise_or )

#bitwise XOR: the differences
bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow("Xor", bitwise_xor)

#bitwise not 
bitwise_not = cv.bitwise_not(rectangle, circle) #
cv.imshow("Bitwise not", bitwise_not)



cv.waitKey(0)