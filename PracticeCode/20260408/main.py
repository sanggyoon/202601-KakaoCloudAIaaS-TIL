import cv2
import numpy as np
import pytesseract

class OCRPreprocessor:

  def __init__(self):
    pass

  def convert_to_grayscale(self, image):
    """
    컬러 이미지를 그레이스케일로 변환
    """

    if len(image.shape) == 3:
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
      gray = image.copy()
    return gray
  
  def apply_threshold(self, image, method='adaptive'):
    """
    이미지에 이진화 처리를 적용하여 흑백으로 변환
    """

    gray = self.convert_to_grayscale(image)

    if method == 'simple':
      _, thresh - cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    elif method == 'adaptive':
      thres = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
      )

    elif method == 'otsu':
      _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2,THRESH_OTSU
      )

    return thresh
  
  def remove_noise(self, image):
    """
    이진화된 이미지에서 노이즈를 제거
    """

    kernel = np.ones((3,3,), np.uint8)

    opening = cv2.morphologyEx(image, cv2.MORTH_OPEN, kernel)

    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    denoised = cv2.GaussianBlur(closing, (3,3), 0)