import cv2
import numpy as np
import pytesseract

def create_sample_image():
  """테스트용 샘플 이미지 생성"""
  image = np.ones((200, 600, 3), dtype=np.uint8) * 255

  font = cv2.FONT_HERSHEY_SIMPLEX

  cv2.putText(image, 'Hello OCR World!', (50, 100), font, 2, (0,0,0), 3)
  cv2.putText(image, 'This is a test image', (50, 150), font, 1, (0,0,0), 2)

  cv2.imwrite('sample_text.jpg', image)
  return image

def basic_ocr_example():
  """가장 기본적인 OCR 예제"""
  image_path = "sample_text4.jpg"
  image = cv2.imread(image_path)

  if image is None:
    print("이미지를 찾을 수 없습니다.")
    image = create_sample_image()

  text = pytesseract.image_to_string(image, lang='eng')

  print("인식된 테스트: ")
  print(text)

  return text,image

text, image = basic_ocr_example()


