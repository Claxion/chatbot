import json
import requests
from datetime import datetime

def main():
    # test 채널에 webhook으로 메시지를 보낸다.
    webhook_url = "https://hooks.slack.com/services/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"
    content = "안녕하세요"
    payload = {"text": content}
 
    requests.post(
        webhook_url, data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
 
 
if __name__ == '__main__':
    main()


# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract

# # If you don't have tesseract executable in your PATH, include the following:
# #full path 
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\python\for_myself'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# # Simple image to string
# print(pytesseract.image_to_string(Image.open('식단.png')))

# # French text image to string
# print(pytesseract.image_to_string(Image.open('식단.jpg'), lang='ko-kr'))

# # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# # NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# # Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))

# # Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')

# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')