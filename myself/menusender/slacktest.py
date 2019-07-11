import json
import requests
import imutils
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# slack 메시지 전달프로그램
# def main():
#     # test 채널에 webhook으로 메시지를 보낸다.
#     webhook_url = "https://hooks.slack.com/services/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"
#     content = "안녕하세요"
#     payload = {"text": content}
 
#     requests.post(
#         webhook_url, data=json.dumps(payload),
#         headers={'Content-Type': 'application/json'}
#     )
 
 
# if __name__ == '__main__':
#     main()


def setLabel(image, str, contour):
    (text_width, text_height), baseline = cv2.getTextSize(str, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)
    x,y,width,height = cv2.boundingRect(contour)
    pt_x = x+int((width-text_width)/2)
    pt_y = y+int((height + text_height)/2)
    cv2.rectangle(image, (pt_x, pt_y+baseline), (pt_x+text_width, pt_y-text_height), (200,200,200), cv2.FILLED)
    cv2.putText(image, str, (pt_x, pt_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, 8)



########### 이미지 전처리 과정 ##########
# https://webnautes.tistory.com/1296
# https://sosal.kr/1067
# https://076923.github.io/posts/Python-opencv-9/#top
import cv2 
import numpy as np

image_address = r'C:\Users\student\python\myself\menusender'

img_color = cv2.imread(image_address+ r"\menu.png", cv2.IMREAD_COLOR)
copy_img = img_color.copy()
img_gray = cv2.cvtColor(copy_img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Show Image', img_gray)
cv2.waitKey(0)
cv2.imwrite(image_address+r"\savedimage.jpg", img_gray)
cv2.destroyAllWindows()

## 흑백처리 완료
# blur 
img_gray_blurred = cv2.GaussianBlur(img_gray, (5,5),0)

# 목표는 선을 명확히해서 주변 둘레 선을 확인하는 것이다.
ret,img_binary = cv2.threshold(img_gray_blurred, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
cv2.imshow('result', img_binary)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rectlist = []
for cnt in contours:
    size = len(cnt)
    print(size)

    epsilon = 0.005 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    size = len(approx)
    print(size)

    cv2.line(img_gray_blurred, tuple(approx[0][0]), tuple(approx[size-1][0]), (0, 255, 0), 3)
    for k in range(size-1):
        cv2.line(img_gray_blurred, tuple(approx[k][0]), tuple(approx[k+1][0]), (0, 255, 0), 3)

    if cv2.isContourConvex(approx):
        if size == 3:
            setLabel(img_gray_blurred, "triangle", cnt)
        elif size == 4:
            #setLabel(img_gray_blurred, "rectangle", cnt)
            rectlist.append(cnt)
        elif size == 5:
            setLabel(img_gray_blurred, "pentagon", cnt)
        elif size == 6:
            setLabel(img_gray_blurred, "hexagon", cnt)
        elif size == 8:
            setLabel(img_gray_blurred, "octagon", cnt)
        elif size == 10:
            setLabel(img_gray_blurred, "decagon", cnt)
        else:
            setLabel(img_gray_blurred, str(size), cnt)
    else:
        setLabel(img_gray_blurred, str(size), cnt)

cv2.imshow('result', img_gray)
cv2.waitKey(0)

# rentangle 2가지 찾음 -> 2을 각각을 이미지로 저장하자
count = 0
for rect in rectlist : 
    rect = rect.astype("float")
    rect = rect.astype("int")
    x,y,w,h = cv2.boundingRect(rect)

    if w < 200: 
        continue
    count += 1
    cv2.imwrite(image_address+r"/Img"+str(count)+".jpg", img_gray[y: y + h, x: x + w])

src = cv2.imread(image_address+r"/Img1.jpg", cv2.IMREAD_GRAYSCALE)
rectdst = src.copy() 
roi = src[100:600, 200:700]
rectdst[0:600, 0:600] = roi

cv2.imshow("src", src)
cv2.imshow("dst", rectdst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 격자감지 https://codeday.me/ko/qa/20190619/823855.html
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html

# img = cv2.imread(image_address + '\Img1.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
  
# # Apply edge detection method on the image 
# edges = cv2.Canny(gray,50,150,apertureSize = 3) 
  
# # This returns an array of r and theta values 
# lines = cv2.HoughLines(edges,1,np.pi/180, 200) 

# # The below for loop runs till r and theta values  
# # are in the range of the 2d array 
# for r,theta in lines[0]: 
    
#     print(lines[1])
#     # Stores the value of cos(theta) in a 
#     a = np.cos(theta) 
#     # Stores the value of sin(theta) in b 
#     b = np.sin(theta) 
#     # x0 stores the value rcos(theta) 
#     x0 = a*r 
#     # y0 stores the value rsin(theta) 
#     y0 = b*r 
#     # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
#     x1 = int(x0 + 1000*(-b))    
#     # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
#     y1 = int(y0 + 1000*(a)) 
#     # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
#     x2 = int(x0 - 1000*(-b)) 
#     # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
#     y2 = int(y0 - 1000*(a)) 
#     # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
#     # (0,0,255) denotes the colour of the line to be  
#     #drawn. In this case, it is red.  
#     cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2) 
      
# # All the changes made in the input image are finally 
# # written on a new image houghlines.jpg 
# cv2.imwrite(image_address + '\houghlines3.jpg',img)

## pytesseract 사용


# If you don't have tesseract executable in your PATH, include the following:
#full path 
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\python\myself\menusender'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string : basic english
#print(pytesseract.image_to_string(Image.open(image_address +'\savedimage.jpg')))

# korean text image to string -> 전체 이미지 대상
totalstr = pytesseract.image_to_string(Image.open(image_address + '\Img1.jpg'), lang='kor')
print(totalstr)
totalstrlist = totalstr.split(' ')
strlist = list(filter(None, totalstrlist))
print(strlist)
#print(pytesseract.image_to_string(Image.open(image_address + '\Img2.jpg'), lang='kor'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# # Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))