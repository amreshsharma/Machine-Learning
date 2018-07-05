import cv2

img = cv2.imread('./images/messi1.jpg')

img_resize = cv2.resize(img,(320,400))

cv2.imshow('image',img_resize)
cv2.waitKey(0)

# create new images
cv2.imwrite('./images/messigray.png',img_resize)
cv2.destroyAllWindows()
