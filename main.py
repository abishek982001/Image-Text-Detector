from textDetector import *
from text_to_speech import *

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
boundingBox = BoundingBox()
while(True):

    print("*****Menu*****")
    print("1. Detect characters in image")
    print("2. Detect words in image")
    print("3. Quit")
    choice = int(input("Enter your choice:"))
    if choice > 3 or choice < 1:
        print("Invalid choice")
        continue
    if choice == 3:
        print("Quitting...")
        exit(0)

    try:
        path = input("Enter the path of the image:")
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except:
        print("Invalid path")
        continue
    output_text = input("Do you want the detected text to be printed in the image Enter (yes/no)")
    if output_text.lower() == 'no':
        flag = False
    elif output_text.lower() == 'yes':
        flag = True
    else:
        print("Invalid input")
        continue
    if choice == 1:
        boundingBox.detect_characters(image, flag)
    if choice == 2:
        words = boundingBox.detect_words(image, flag)

    cv2.imshow("Result", image)
    cv2.waitKey(0)