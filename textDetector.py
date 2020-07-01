import cv2
import pytesseract


def detect_characters(putText=False):
    """Function that detects text and draws boxes character by character"""
    image_height, image_width,_ = image.shape
    boxes = pytesseract.image_to_boxes(image)
    for box_info in boxes.splitlines():
        box_info = box_info.split(' ')
        # print(box_info)
        x,y,w,h = int(box_info[1]), int(box_info[2]), int(box_info[3]), int(box_info[4])  # Get the coordinates to draw boxes
        cv2.rectangle(image, (x,image_height-y), (w,image_height-h), (0,0,255), 2)  # Draws the boxes
        if putText == True:
            cv2.putText(image, box_info[0], (x, image_height-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)

def detect_words(putText=False):
    """Function that detects words and draws boxes"""
    image_height, image_width,_ = image.shape
    boxes = pytesseract.image_to_data(image)
    for count, box_info in enumerate(boxes.splitlines()):
        if count!=0:
            box_info = box_info.split()
            # print(box_info)
            if len(box_info)==12:
                x,y,w,h = int(box_info[6]), int(box_info[7]), int(box_info[8]), int(box_info[9])  # Get the coordinates to draw boxes
                cv2.rectangle(image, (x,y), (w+x,h+y), (0,0,255), 3)
                if putText == True:
                    cv2.putText(image, box_info[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)

def detect_digits_only(putDigit=False):
    """Function that detects digits only"""
    image_height, image_width,_ = image.shape
    confg = r'--oem 3 --psm 6 outputbase digits'  # Configure tesseract to detect digits only
    boxes = pytesseract.image_to_data(image, config=confg)
    for count, box_info in enumerate(boxes.splitlines()):
        if count!=0:
            box_info = box_info.split()
            # print(box_info)
            if len(box_info)==12:
                x,y,w,h = int(box_info[6]), int(box_info[7]), int(box_info[8]), int(box_info[9])  # Get the coordinates to draw boxes
                cv2.rectangle(image, (x,y), (w+x,h+y), (0,0,255), 3)
                if putDigit == True:
                    cv2.putText(image, box_info[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

while(True):

    print("*****Menu*****")
    print("1. Detect characters in image")
    print("2. Detect words in image")
    print("3. Quit")
    choice = int(input("Enter your choice:"))
    if choice > 3 or choice < 1:
        print("Invlid choice")
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
        detect_characters(flag)
    if choice == 2:
        detect_words(flag)

    cv2.imshow("Result", image)
    cv2.waitKey(0)
