import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread('test.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract.image_to_string(img)
cv2.imshow("Result", img)
cv2.waitKey(0)
