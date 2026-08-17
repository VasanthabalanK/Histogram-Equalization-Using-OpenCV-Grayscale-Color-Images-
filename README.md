# Histogram-Equalization-Using-OpenCV-Grayscale-Color-Images
# NAME: VASANTHABALAN K
# REG.NO: 212224230296
# Aim
To write a Python program using OpenCV to perform histogram equalization on both grayscale and color images to enhance image contrast and brightness.
# Software Used
Anaconda – Python 3.7
Jupyter Notebook / VS Code
OpenCV (cv2)
NumPy
Matplotlib
# Algorithm
# Step 1:
Import the required libraries: OpenCV, NumPy, and Matplotlib.

# Step 2:
Read the image parrot.jpg in grayscale format.

# Step 3:
Display the grayscale image and plot its histogram.

# Step 4:
Apply histogram equalization using cv2.equalizeHist() to enhance contrast.

# Step 5:
Display original grayscale image, its histogram, enhanced image, and its histogram using a 2 × 2 grid.

# Step 6:
Read the same image in color format.

# Step 7:
Split the image into B, G, R channels and plot their histograms.

# Step 8:
Convert the image from BGR to HSV color space.

# Step 9:
Apply histogram equalization on the V (Value) channel.

# Step 10:
Merge the channels and convert the image back to BGR format.

# Step 11:
Display original color image, histogram, enhanced image, and enhanced histogram using a 2 × 2 grid.

# Program
# 1. Import the required libraries and read the grayscale image.
```
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('parrot.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()
```
# 2. Plot the histogram of the grayscale image.
```
plt.hist(img.ravel(), 256, range=[0,256])
plt.title('Original Image Histogram')
plt.show()
```
# 3. Apply histogram equalization.
```
img_eq = cv2.equalizeHist(img)
```
# 4. Display the histogram of the equalized image.
```
plt.hist(img_eq.ravel(), 256, range=[0,256])
plt.title('Equalized Histogram')
plt.show()
```
# 5. Display the equalized grayscale image.
```
plt.imshow(img_eq, cmap='gray')
plt.title('Equalized Image')
plt.show()
```
# 6. Read the image in color mode and convert to HSV.
```
img = cv2.imread('gta.jpg', cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```
# 7. Apply histogram equalization to the V channel.
```
img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
```
# 8. Convert the enhanced HSV image back to BGR.
```
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
```
# 9. Display the original and equalized color images.
```
plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')

plt.subplot(122)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')

plt.show()
```
# 10. Display the original and equalized images along with their histograms.
```
plt.figure(figsize=[12,10])

plt.subplot(221)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')

plt.subplot(222)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')

plt.subplot(223)
plt.hist(img.ravel(), 256, range=[0,256])
plt.title('Original Histogram')

plt.subplot(224)
plt.hist(img_eq.ravel(), 256, range=[0,256])
plt.title('Histogram Equalized')

plt.show()
```
# OUTPUT:
<img width="552" height="342" alt="image" src="https://github.com/user-attachments/assets/53040e00-65f2-4957-b062-5a126d487a51" />
<img width="561" height="433" alt="image" src="https://github.com/user-attachments/assets/c66bfdb1-e0bf-40da-bd6e-4d0274a69362" />
<img width="561" height="433" alt="image" src="https://github.com/user-attachments/assets/6ccda953-11a2-460b-9108-58c31834a22a" />
<img width="552" height="342" alt="image" src="https://github.com/user-attachments/assets/e7f3ee77-094c-4be7-bc59-4340a5d33b29" />
<img width="552" height="342" alt="image" src="https://github.com/user-attachments/assets/53d514c4-c39e-4230-b7d0-086dfee5c5c2" />
<img width="570" height="433" alt="image" src="https://github.com/user-attachments/assets/bcf9de9e-329c-4c04-9394-b2384c5c6a33" />
<img width="1525" height="414" alt="image" src="https://github.com/user-attachments/assets/8890c0a2-69fe-4977-8058-b478fee5ed18" />
<img width="1236" height="372" alt="image" src="https://github.com/user-attachments/assets/9aaaa3b0-048b-4263-a9dc-cdeab405339f" />

# Result:

Thus, histogram equalization is successfully performed on both grayscale and color images using OpenCV. The contrast and brightness of the images are significantly improved, enhancing visual quality and feature visibility.
