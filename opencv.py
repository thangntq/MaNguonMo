
import cv2
import numpy as np

# Đọc ảnh từ đường dẫn
anh = r"C:\Users\hoang ty\Downloads\image.jpg"
imagex = cv2.imread(anh, cv2.IMREAD_GRAYSCALE)
image= cv2.imread(anh,cv2.IMREAD_COLOR)

# bài 2

# Nhập góc quay từ bàn phím

angle = int(input("Nhập góc quay (độ): "))

#Tính ma trận quay
rows, cols = image.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

# Xoay ảnh
rotated_image = cv2.warpAffine(image, M, (cols, rows))

# Hiển thị ảnh sau khi xoay
cv2.imshow('anh xam', imagex)
cv2.imshow('anh goc', image)
cv2.imshow('anh da xoay', rotated_image)

# bài 3

final = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
cv2.imshow('anh chuan hoa',final)


# bài4
# Đọc ảnh từ đường dẫn
anh2 = r"C:\Users\hoang ty\Pictures\Camera Roll\hoa.jpg"
image1 = cv2.imread(anh2, cv2.IMREAD_COLOR)

# Phát hiện biên bằng Canny ở 3 mức độ khác nhau
canny1 = cv2.Canny(image1, 50, 50)
canny2 = cv2.Canny(image1, 50, 200)
canny3 = cv2.Canny(image1, 150, 250)

# Hiển thị ảnh gốc và biên ở 3 mức độ khác nhau
cv2.imshow('anh goc2', image1)
cv2.imshow('anh bien1', canny1)
cv2.imshow('anh bien2', canny2)
cv2.imshow('anh bien3', canny3)
cv2.waitKey(0)

# Đóng cửa sổ khi hoàn thành
cv2.destroyAllWindows()