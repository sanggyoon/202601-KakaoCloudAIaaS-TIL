import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_iou(box1, box2):
  x1_inter = max(box1[0], box2[0])
  y1_inter = max(box1[1], box2[1])
  x2_inter = min(box1[2], box2[2])
  y2_inter = min(box1[3], box2[3])

  if x2_inter <= x1_inter or y2_inter <= y1_inter:
    return 0.0
  
  intersection_area = (x2_inter - x1_inter) * (y2_inter - y1_inter)

  box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
  box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

  union_area = box1_area + box2_area - intersection_area
  
  return intersection_area / union_area

def nms(boxes, scores, iou_threshold=0.5):
  indices = np.argsort(scores)[::-1]
  keep = []

  while len(indices) > 0:
    current = indices[0]
    keep.append(current)

    if len(indices) == 1:
      break

    current_box = boxes[current]
    other_boxes = boxes[indices[1:]]

    ious = []
    for other_box in other_boxes:
      iou = calculate_iou(current_box, other_box)
      ious.append(iou)

    ious = np.array(ious)

    indices = indices[1:][ious < iou_threshold]

  return keep

def visualize_nms():
  boxes = np.array([
    [50, 50, 150, 150],
    [60, 60, 160, 160],
    [200, 100, 300, 200],
    [210, 110, 310, 210],
    [70, 70, 170, 170]
  ])

  scores = np.array([0.9, 0.8, 0.85, 0.7, 0.75])

  keep_indices = nms(boxes, scores, iou_threshold=0.3)

  plt.rc('font', family='AppleGothic')
  fig, axes = plt.subplots(1, 2, figsize=(15, 6))

  img = np.ones((350, 400, 3)) * 0.9
  axes[0].imshow(img)
  axes[0].set_title('NMS 적용 전')

  colors = ['red', 'blue', 'green', 'orange', 'purple']

  for i, (box, score) in enumerate(zip(boxes, scores)):
    x1, y1, x2, y2 = box

    rect = patches.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=2, edgecolor=colors[i], facecolor=colors[i], alpha=0.3)  
    axes[0].add_patch(rect)
    axes[0].text(x1, y1-5, f'Box {i+1}: {score:.2f}', color=colors[i], fontsize=10, weight='bold')

  axes[0].set_xlim(0, 400)
  axes[0].set_ylim(350, 0)
  axes[0].axis('off')

  axes[1].imshow(img)
  axes[1].set_title('NMS 적용 후')

  for i in keep_indices:
    box, score = boxes[i], scores[i]
    x1, y1, x2, y2 = box
    rect = patches.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=3, edgecolor=colors[i], facecolor=colors[i], alpha=0.3)
    
    axes[1].add_patch(rect)
    axes[1].text(x1, y1-5, f'Box {i+1}: {score:.2f}', color=colors[i], fontsize=10, weight='bold')

  axes[1].set_xlim(0, 400)
  axes[1].set_ylim(350, 0)
  axes[1].axis('off')

  plt.tight_layout()
  plt.show()

  print(f"원본 박스 수: {len(boxes)}")
  print(f"NMS 후 박스 수: {len(keep_indices)}")
  print(f"제거된 박스: {[i+1 for i in range(len(boxes)) if i not in keep_indices]}")

visualize_nms()