import cv2 
import numpy as np
import imutils
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import tabledetect 

def setLabel(image, str, contour):
    (text_width, text_height), baseline = cv2.getTextSize(str, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)
    x,y,width,height = cv2.boundingRect(contour)
    pt_x = x+int((width-text_width)/2)
    pt_y = y+int((height + text_height)/2)
    cv2.rectangle(image, (pt_x, pt_y+baseline), (pt_x+text_width, pt_y-text_height), (200,200,200), cv2.FILLED)
    cv2.putText(image, str, (pt_x, pt_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, 8)


def changeGrayColorAndBlur(address) : 
    ########### 이미지 전처리 과정 ##########
    # https://webnautes.tistory.com/1296
    # https://sosal.kr/1067
    # https://076923.github.io/posts/Python-opencv-9/#top
    img_origin = cv2.imread(address+ r"\menu.png", cv2.IMREAD_COLOR)
    img_copy = img_origin.copy() 
    img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Show Image', img_gray)
    # cv2.waitKey(0)
    cv2.imwrite(address+r"\menu_gray.jpg", img_gray)
    # 가우시안을 이용해서 이미지를 조금 더 명확하게 구분할 수 있게 된다고 한다.
    ##블러가 필요한가?
    img_blurred = cv2.GaussianBlur(img_gray,(5,5), 0)
    # cv2.imshow('Show Image', img_blurred)
    # cv2.waitKey(0)
    cv2.imwrite(address+r"\menu_blurred.jpg", img_blurred)
    # cv2.destroyAllWindows()
    print("이미지 전처리 - 흑백화 및 블러 완료")
    
# 이 함수를 통해 그림에서 필요한 부분만을 잘라낸다.     
# 목표는 선을 명확히해서 주변 둘레 선을 확인하는 것이다.
# https://webnautes.tistory.com/1097

def saveBoxImage(address) : 

    img = cv2.imread(address+ r"\menu.png", cv2.IMREAD_GRAYSCALE)

    ret,img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    #cv2.imshow('result', img_binary)
    #cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectlist = []
    for cnt in contours:
        size = len(cnt)
        
        epsilon = 0.005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        size = len(approx)
        
        cv2.line(img, tuple(approx[0][0]), tuple(approx[size-1][0]), (0, 255, 0), 3)
        for k in range(size-1):
            cv2.line(img, tuple(approx[k][0]), tuple(approx[k+1][0]), (0, 255, 0), 3)

        if cv2.isContourConvex(approx):
            if size == 3:
                setLabel(img, "triangle", cnt)
            elif size == 4:
                #setLabel(img, "rectangle", cnt)
                rectlist.append(cnt)
            elif size == 5:
                setLabel(img, "pentagon", cnt)
            elif size == 6:
                setLabel(img, "hexagon", cnt)
            elif size == 8:
                setLabel(img, "octagon", cnt)
            elif size == 10:
                setLabel(img, "decagon", cnt)
            else:
                setLabel(img, str(size), cnt)
        else:
            setLabel(img, str(size), cnt)

    # rentangle 2가지 찾음 -> 2을 각각을 이미지로 저장하자
    count = 0
    for rect in rectlist : 
        rect = rect.astype("float")
        rect = rect.astype("int")
        x,y,w,h = cv2.boundingRect(rect)

        if w < 200: 
            continue
        count += 1
        cv2.imwrite(address+r"/menuBox"+str(count)+".jpg", img[y: y + h, x: x + w])

    
def cutImagesToGetInfo(address, imagename) : 
    # http://www.gisdeveloper.co.kr/?p=6714
    # 먼저 Box1 : 식단표
    # Box2 : 반시간표
    # 혹시 형태가 바뀐다면 크기에 따라서 바꿔주는 것이 맞을 듯하다. 큰 것이 식단표. 위의 함수에서 저장해줄 때 처리해주면 됨.
    # 격자감지 https://codeday.me/ko/qa/20190619/823855.html
    # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    # Hough Transform 방법
    # https://answers.opencv.org/question/63847/how-to-extract-tables-from-an-image/ 테이블 찾아내서 잘라내기 
    # file:///C:/Users/student/Downloads/opencv-python-tutroals.pdf
    # https://m.blog.naver.com/samsjang/220505815055

    img = cv2.imread(f"{address}\{imagename}.jpg")
    cv2.imshow("img",img)
    mask,joint = tabledetect.detectTable(img).run()
    cv2.waitKey()

    corners = cv2.goodFeaturesToTrack(joint,50,0.1,10)
    corners = np.int0(corners)
    # 일단 찾은 x,y = corner.ravel() 를 set에 넣고, 약 차이가 5 미만인 것은 그 중 가장 작은 값으로 통일한다. 같은 라인인데 약간의 오차로 만들어진 놈들임
    xset = set() 
    yset = set()
    xylist = dict() 
    number = 1
    for corner in corners :
        x,y = corner.ravel()
        xset.add(x)
        yset.add(y)
        xylist[number] = { 'x' : x , 'y' : y}
        cv2.circle(mask, (x,y),5 ,(0,0,255),-1)
        number += 1
    
    print(xylist)
    

    cv2.imshow("img",mask)
    cv2.waitKey()

    


def makeMenuItems(address) : 
    print("메뉴만들기")
    changeGrayColorAndBlur(address)
    saveBoxImage(address) 
    
    #날짜를 찾아서
    #필요한 만큼 잘라야 할 것 같다.   
    #cutImagesToGetInfo(address, "menuBox1")
    cutImagesToGetInfo(address, "menuBox2")

    

    

    ## pytesseract 사용


    # If you don't have tesseract executable in your PATH, include the following:
    #full path 
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\python\myself\menusender'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Simple image to string : basic english
    #print(pytesseract.image_to_string(Image.open(address +'\savedimage.jpg')))

    # korean text image to string -> 전체 이미지 대상
    totalstr = pytesseract.image_to_string(Image.open(address + '\menuBox1.jpg'), lang='kor')
    print(totalstr)
    totalstrlist = totalstr.split(' ')
    strlist = list(filter(None, totalstrlist))
    print(strlist)
    #print(pytesseract.image_to_string(Image.open(address + '\Img2.jpg'), lang='kor'))

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