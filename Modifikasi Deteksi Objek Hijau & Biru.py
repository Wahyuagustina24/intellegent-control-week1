import cv2
import numpy as np

#Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Rentang warna biru dalam HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    #Rentang warna hijau dalam HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    #Masking untuk mendeteksi warna biru
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    result_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    #Masking untuk mendeteksi warna hijau
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    result_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    
    #Menampilkan hasil
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask Blue", mask_blue)
    cv2.imshow("Result Blue", result_blue)
    cv2.imshow("Mask Green", mask_green)
    cv2.imshow("Result Green", result_green)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()