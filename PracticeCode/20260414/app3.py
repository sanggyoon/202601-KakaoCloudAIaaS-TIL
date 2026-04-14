import cv2
import numpy as np
import streamlit as st

st.title('OpenCV 색상 분할 & 객체 탐지')

tab1, tab2 = st.tabs(['색상 분할 (HSV)', '윤곽선 탐지'])

with tab1:
  st.subheader('색상 객체 분리')
  uploaded = st.file_uploader('이미지 업로드', type=['jpg', 'jpeg', 'png'], key='tab1')

  st.markdown('**Hue (색상)**')
  col1, col2 = st.columns(2)
  lower_h = col1.slider('Hue 최소', 0, 179, 100)
  upper_h = col2.slider('Hue 최대', 0, 179, 140)

  st.markdown('**Saturation (채도)**')
  col3, col4 = st.columns(2)
  lower_s = col3.slider('Saturation 최소', 0, 255, 150)
  upper_s = col4.slider('Saturation 최대', 0, 255, 255)

  st.markdown('**Value (명도)**')
  col5, col6 = st.columns(2)
  lower_v = col5.slider('Value 최소', 0, 255, 0)
  upper_v = col6.slider('Value 최대', 0, 255, 255)

  if uploaded:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([lower_h, lower_s, lower_v])
    upper = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv_image, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    col1, col2, col3 = st.columns(3)
    col1.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='원본', use_container_width=True)
    col2.image(mask, caption='마스크', use_container_width=True)
    col3.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='분리 결과', use_container_width=True)

with tab2:
  st.subheader('가장 큰 객체 윤곽선 탐지')
  uploaded2 = st.file_uploader('이미지 업로드', type=['jpg', 'jpeg', 'png'], key='tab2')

  if uploaded2:
    file_bytes = np.frombuffer(uploaded2.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
      largest_contour = max(contours, key=cv2.contourArea)

      mask = np.zeros(image.shape[:2], dtype=np.uint8)
      cv2.drawContours(mask, [largest_contour], -1, 255, -1)
      segmented_object = cv2.bitwise_and(image, image, mask=mask)

      contour_image = image.copy()
      cv2.drawContours(contour_image, [largest_contour], -1, (0, 255, 0), 3)

      col1, col2, col3 = st.columns(3)
      col1.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='원본', use_container_width=True)
      col2.image(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB), caption='윤곽선', use_container_width=True)
      col3.image(cv2.cvtColor(segmented_object, cv2.COLOR_BGR2RGB), caption='분리 결과', use_container_width=True)

      st.write(f'탐지된 윤곽선 수: **{len(contours)}개**')
      st.write(f'가장 큰 객체 면적: **{cv2.contourArea(largest_contour):.0f}px²**')
    else:
      st.warning('윤곽선을 찾지 못했습니다.')
