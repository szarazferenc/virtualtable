import cv2
import numpy as np

# Kép beolvasása
image = cv2.imread('testpic.png', cv2.IMREAD_COLOR)

# Kép átméretezése (opcionális)
# image = cv2.resize(image, (new_width, new_height))

# Szürkeárnyalatosra konvertálás
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Körök keresése a Hough transzformációval
circles = cv2.HoughCircles(
    gray,                  # Bemeneti kép
    cv2.HOUGH_GRADIENT,    # Detekciós módszer
    dp=16,                  # Képméretarány
    minDist=100,            # Minimum távolság két kör között
    param1=50,             # Canny élek paraméter
    param2=30,             # A Hough transzformáció küszöbértéke
    minRadius=100,          # Minimum kör sugara
    maxRadius=300          # Maximum kör sugara
)

# Ellenőrizze, hogy talált-e köröket
if circles is not None:
    # Körök koordinátáinak kinyerése és rajzolása
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        # Kör rajzolása a képre
        cv2.circle(image, center, radius, (0, 255, 0), 2)

    # Eredeti és eredmény képek megjelenítése
    cv2.imshow('OrigPic', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Nem talált köröket.')

