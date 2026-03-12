import sys
import cv2
from PyQt6.QtWidgets import QApplication, QFileDialog

# ---------- CLEAN IMAGE PICKER ----------
app = QApplication(sys.argv)

file_path, _ = QFileDialog.getOpenFileName(
    None,
    "Choose an Image",
    "",
    "Images (*.png *.jpg *.jpeg)"
)

if not file_path:
    print("No image selected")
    sys.exit()

# ---------- LOAD IMAGE ----------
img = cv2.imread(file_path)

mode = 0   # 0=normal, 1=gray, 2=vintage, 3=dramatic

# ---------- MAIN LOOP ----------
while True:

    display_img = img.copy()

    key = cv2.waitKey(25) & 0xFF

    # ---- CHANGE MODE ----
    if key == ord('1'):
        mode = 1

    if key == ord('2'):
        mode = 2

    if key == ord('3'):
        mode = 3

    if key == ord('r'):
        mode = 0

    if key == ord(' '):
        break

    # ---- APPLY FILTERS ----
    if mode == 1:
        display_img = cv2.cvtColor(display_img, cv2.COLOR_BGR2GRAY)
        cv2.putText(display_img, "GRAY", (150,150),
                    cv2.FONT_HERSHEY_DUPLEX, 2, (255,255,255), 2)

    elif mode == 2:
        display_img = cv2.add(display_img, (0,0,90))
        display_img = cv2.subtract(display_img, (90,0,0))
        cv2.putText(display_img, "VINTAGE", (150,150),
                    cv2.FONT_HERSHEY_DUPLEX, 2, (170,200,35), 2)

    elif mode == 3:
        display_img = cv2.convertScaleAbs(display_img, alpha=3, beta=50)
        cv2.putText(display_img, "DRAMATIC", (150,150),
                    cv2.FONT_HERSHEY_DUPLEX, 2, (170,200,35), 2)

    # ---- SHOW IMAGE ----
    cv2.imshow("Photo Editor", display_img)

cv2.destroyAllWindows()
