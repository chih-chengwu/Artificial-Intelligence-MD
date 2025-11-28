# 首先，導入了OpenCV和NumPy庫。
import cv2
import numpy as np

# 定義一個函數 apply_convolution，該函數使用 cv2.filter2D 函數應用卷積核到圖像上。
def apply_convolution(image, kernel):
    return cv2.filter2D(image, -1, kernel)

# 讀取原始圖像，並轉換成灰階圖
image = cv2.imread('house.jpg', cv2.IMREAD_GRAYSCALE)

# 定義直線、橫線和斜線卷積核
kernel_vertical = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]])

kernel_horizontal = np.array([[-1, -1, -1],
                              [0, 0, 0],
                              [1, 1, 1]])

kernel_diagonal = np.array([[1, 0, -1],
                            [0, 0, 0],
                            [-1, 0, 1]])

# 應用卷積核並獲取特征圖
vertical_feature = apply_convolution(image, kernel_vertical)
horizontal_feature = apply_convolution(image, kernel_horizontal)
diagonal_feature = apply_convolution(image, kernel_diagonal)

# 顯示原圖和特征圖
cv2.imshow('Original Image', image)
cv2.imshow('Vertical Feature', vertical_feature)
cv2.imshow('Horizontal Feature', horizontal_feature)
cv2.imshow('Diagonal Feature', diagonal_feature)

# 保存特徵圖到與程式相同的文件夾
cv2.imwrite('vertical_feature.jpg', vertical_feature)
cv2.imwrite('horizontal_feature.jpg', horizontal_feature)
cv2.imwrite('diagonal_feature.jpg', diagonal_feature)

#等待按鍵輸入（cv2.waitKey(0)）並在任何按鍵被按下後關閉所有打開的視窗（cv2.destroyAllWindows()）。
cv2.waitKey(0)
cv2.destroyAllWindows()