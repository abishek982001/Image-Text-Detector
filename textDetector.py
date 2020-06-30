import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
image = cv2.imread('test.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(image))

def detect_characters():
    """Function that detects text and draws boxes character by character"""
    image_height, image_width,_ = image.shape
    boxes = pytesseract.image_to_boxes(image)
    for box_info in boxes.splitlines():
        box_info = box_info.split(' ')
        # print(box_info)
        x,y,w,h = int(box_info[1]), int(box_info[2]), int(box_info[3]), int(box_info[4])  # Get the coordinates to draw boxes
        cv2.rectangle(image, (x,image_height-y), (w,image_height-h), (0,0,255), 2)  # Draws the boxes
        cv2.putText(image, box_info[0], (x, image_height-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


detect_characters()
cv2.imshow("Result", image)
cv2.waitKey(0)
