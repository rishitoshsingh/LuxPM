import cv2
import numpy as np

def task1(image):
    _, width, _ = image.shape
    
    x_translate = width * 0.25
    M = np.float32([[1, 0, x_translate], [0, 1, 0]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imwrite('task1.jpg', shifted)

def task2(image):
    height, _ , _ = image.shape
    
    y_translate = height * 0.25
    M = np.float32([[1, 0, 0], [0, 1, y_translate]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imwrite('task2.jpg', shifted)

def task3(image):
    height, width, _ = image.shape
    center = (width // 2, height // 2)
    
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (width, height))
    cv2.imwrite('task3.jpg', rotated)
    
def task4(image):
    height, width, _ = image.shape
    center = (width // 2, height // 2)
    
    M = cv2.getRotationMatrix2D(center, -90, 1.0)
    rotated = cv2.warpAffine(image, M, (width, height))
    cv2.imwrite('task4.jpg', rotated)
    

def task5(image):
    height, width, _ = image.shape
    center = (height // 2, width // 2)
    
    for i in range(50, 0, -1):
        diff = 50 - i
        if diff == 0:
            image[center[0]-diff : center[0]+diff+1 ,center[1]+diff] = np.clip(image[center[0]-diff : center[0]+diff+1 ,center[1]+diff] * (1 + i/100), 0, 255)         
        else:
            image[center[0]-diff : center[0]+diff+1 ,center[1]-diff] = np.clip(image[center[0]-diff : center[0]+diff+1 ,center[1]-diff] * (1 + i/100), 0, 255)
            image[center[0]-diff : center[0]+diff+1 ,center[1]+diff] = np.clip(image[center[0]-diff : center[0]+diff+1 ,center[1]+diff] * (1 + i/100), 0, 255)
            image[center[0]-diff, center[1]-diff+1 : center[1]+diff] = np.clip(image[center[0]-diff, center[1]-diff+1 : center[1]+diff] * (1 + i/100), 0, 255)
            image[center[0]+diff, center[1]-diff+1 : center[1]+diff] = np.clip(image[center[0]+diff, center[1]-diff+1 : center[1]+diff] * (1 + i/100), 0, 255)
    cv2.imwrite('task5.jpg',image)


image = cv2.imread('images.jpg')

task1(image.copy())
task2(image.copy())
task3(image.copy())
task4(image.copy())
task5(image.copy())