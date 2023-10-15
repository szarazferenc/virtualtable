import cv2
import numpy as np

# Kép beolvasása
image = cv2.imread('octagon_image.png', cv2.IMREAD_COLOR)

# Kép átméretezése (opcionális)
# image = cv2.resize(image, (new_width, new_height))

# Szürkeárnyalatosra konvertálás
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Körök keresése a Hough transzformációval
contours, _ = cv2.findContours(
    gray,                   # Bemeneti kép
    cv2.RETR_EXTERNAL,      # Kontúrok keresése csak a külső kontúrokból
    cv2.CHAIN_APPROX_SIMPLE # Kontúrpontok egyszerűsítése
)

# Nyolcszögek keresése
octagons = []
for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 8:
        octagons.append(approx)

# Nyolcszögek kijelölése a képen
for octagon in octagons:
    cv2.drawContours(image, [octagon], 0, (0, 255, 0), 2)

# Eredeti és eredmény képek megjelenítése
cv2.imshow('Eredeti kép', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
