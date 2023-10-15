import cv2

# Webkamera inicializálása
cap = cv2.VideoCapture(0)  # Az 0 jelzi, hogy az első elérhető webkamerát használja

while True:
    # Kép beolvasása a webkamerából
    ret, frame = cap.read()

    if not ret:
        print("Hiba a kép beolvasásakor")
        break

    # Itt add meg a képfeldolgozást, például a körök keresését

    # Kijelzés a képernyőn
    cv2.imshow('Webkamera', frame)

    # Kilépés a 'q' lenyomásával
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kapcsolat bontása és ablakok bezárása
cap.release()
cv2.destroyAllWindows()
