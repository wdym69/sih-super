import PIL.Image
import pytesseract
import cv2

myconfig = r"--psm 11 --oem 3"

img = cv2.imread("image-sih1.png")
height, width, _ = img.shape

# print(pytesseract.image_to_string(Image.open('image-sih1.png')))

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
  box = box.split(" ")
  img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

cv2.imshow("img", img)
# print(pytesseract.image_to_data(Image.open('image-sih1.png')))
cv2.waitKey(0)