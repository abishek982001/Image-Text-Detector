import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
image = cv2.imread('test.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(image))

### Detecting Characters
height_of_image, width_of_image,_ = image.shape
boxes = pytesseract.image_to_boxes(image)
for box_info in boxes.splitlines():
    box_info = box_info.split(' ')
    #print(box_info)
    x,y,w,h = int(box_info[1]), int(box_info[2]), int(box_info[3]), int(box_info[4])  # Get the coordinates to draw boxes
    cv2.rectangle(image, (x,height_of_image-y), (w,height_of_image-h), (0,0,255), 1)  # Draws the boxes

cv2.imshow("Result", image)
cv2.waitKey(0)
