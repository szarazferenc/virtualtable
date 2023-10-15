import cv2
import numpy as np

# Webkamera inicializálása
cap = cv2.VideoCapture(0)  # Az 0 jelzi, hogy az első elérhető webkamerát használja

while True:
    # Kép beolvasása a webkamerából
    ret, frame = cap.read()

    if not ret:
        print("Hiba a kép beolvasásakor")
        break

    # Itt add meg a képfeldolgozást, például a körök keresését
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 25) #cv2.bilateralFilter(gray,10,50,50)
    minDist = 100
    param1 = 20 #optimal:20-30
    param2 = 40 #smaller value-> more false circles
    minRadius = 5
    maxRadius = 100 #max val:100

    # docstring of HoughCircles: HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]])
    circles = cv2.HoughCircles(
        blurred, 
        cv2.HOUGH_GRADIENT, 
        1, 
        minDist, 
        param1=param1, 
        param2=param2, 
        minRadius=minRadius, 
        maxRadius=maxRadius
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(
                frame, 
                (i[0], 
                i[1]), 
                i[2], 
                (0, 255, 0), 
                2
            )
    # Kijelzés a képernyőn
    cv2.imshow('Webkamera with DetectedCircles', frame)

    # Kilépés a 'q' lenyomásával
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kapcsolat bontása és ablakok bezárása
cap.release()
cv2.destroyAllWindows()
