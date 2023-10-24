import cv2
import numpy as np

anh= r"C:\Users\ADMIN\Downloads\picture.jpeg"
img = cv2.imread(anh)
#cv2.imshow('anh_goc',img)      # hiển thị ảnh gốc
#hiển thị ảnh đen trắng
cv2.imshow('anh_den_trang',cv2.imread(anh, cv2.IMREAD_GRAYSCALE))
#tạo 1 ảnh từ png từ ảnh gốc
#cv2.imwrite('anh_den_trang.png',cv2.imread(anh, cv2.IMREAD_GRAYSCALE))

#tạo ảnh mờ
rows, cols = img.shape[:2]    #lấy biên ảnh
kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
kernel_3x3 = np.ones((3,3), np.float32) / 9.0
kernel_5x5 = np.ones((5,5), np.float32) / 25.0
cv2.imshow('Original', img)
output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)
output = cv2.filter2D(img, -5, kernel_3x3)
cv2.imshow('3x3 filter', output)
output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('5x5 filter', output)

#làm mịn ảnh từng khoảng
roi = cv2.selectROI(img)
x, y, w, h = roi
blurred = cv2.GaussianBlur(img[y:y + h, x:x + w], (11, 11), 0)
img[y:y + h, x:x + w] = blurred
cv2.imshow('Blurred Image', img)


cv2.waitKey()