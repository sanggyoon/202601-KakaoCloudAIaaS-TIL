import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision.transforms import functional as F
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

COLORS = [
  (255, 59, 59), (59, 255, 59), (59, 59, 255), (255, 255, 59),
  (255, 59, 255), (59, 255, 255), (255, 140, 59), (140, 59, 255),
]

CLASS_NAMES = [
  '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
  'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
  'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
  'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A',
  'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
  'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
  'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork',
  'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
  'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
  'potted plant', 'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet',
  'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
  'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
  'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

@st.cache_resource
def load_model():
  device = 'cuda' if torch.cuda.is_available() else 'cpu'
  model = maskrcnn_resnet50_fpn(pretrained=True)
  model.to(device)
  model.eval()
  return model, device

def predict(model, device, image, confidence_threshold):
  image_tensor = F.to_tensor(image).unsqueeze(0).to(device)

  with torch.no_grad():
    predictions = model(image_tensor)

  pred = predictions[0]
  keep_idx = pred['scores'] > confidence_threshold

  boxes = pred['boxes'][keep_idx].cpu().numpy()
  labels = pred['labels'][keep_idx].cpu().numpy()
  scores = pred['scores'][keep_idx].cpu().numpy()
  masks = pred['masks'][keep_idx].cpu().numpy()

  return boxes, labels, scores, masks

def overlay_masks(image, masks, boxes, labels, scores):
  result = image.copy().convert('RGBA')

  for i, mask in enumerate(masks):
    color = COLORS[i % len(COLORS)]
    alpha = (mask[0] * 180).astype(np.uint8)
    overlay = Image.new('RGBA', image.size, color + (0,))
    overlay.putalpha(Image.fromarray(alpha))
    result = Image.alpha_composite(result, overlay)

  result = result.convert('RGB')
  draw = ImageDraw.Draw(result)

  for i, (box, label, score) in enumerate(zip(boxes, labels, scores)):
    color = COLORS[i % len(COLORS)]
    x1, y1, x2, y2 = box.astype(int)
    class_name = CLASS_NAMES[label]
    text = f'{class_name} {score:.0%}'

    draw.rectangle([x1, y1, x2, y2], outline=color, width=2)

    text_bbox = draw.textbbox((x1, y1), text)
    draw.rectangle([text_bbox[0] - 2, text_bbox[1] - 2, text_bbox[2] + 2, text_bbox[3] + 2], fill=color)
    draw.text((x1, y1), text, fill=(255, 255, 255))

  return result

st.title('Mask R-CNN 객체 탐지')
st.write('이미지를 업로드하면 객체를 탐지하고 세그멘테이션 마스크를 표시합니다.')

uploaded_file = st.file_uploader('이미지 업로드', type=['jpg', 'jpeg', 'png'])
confidence = st.slider('신뢰도 임계값', 0.0, 1.0, 0.5, 0.05)

if uploaded_file:
  image = Image.open(uploaded_file).convert('RGB')

  col1, col2 = st.columns(2)
  with col1:
    st.subheader('원본 이미지')
    st.image(image, use_container_width=True)

  with st.spinner('모델 로딩 및 분석 중...'):
    model, device = load_model()
    boxes, labels, scores, masks = predict(model, device, image, confidence)

  result_image = overlay_masks(image, masks, boxes, labels, scores)

  with col2:
    st.subheader('탐지 결과')
    st.image(result_image, use_container_width=True)

  st.subheader(f'탐지된 객체: {len(labels)}개')
  for i, (label, score, box) in enumerate(zip(labels, scores, boxes)):
    class_name = CLASS_NAMES[label]
    x1, y1, x2, y2 = box.astype(int)
    st.write(f'**{i+1}. {class_name}** — 신뢰도: {score:.1%} | 위치: ({x1}, {y1}) ~ ({x2}, {y2})')
