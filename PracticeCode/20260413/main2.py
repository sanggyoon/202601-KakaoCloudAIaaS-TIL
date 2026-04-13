import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def visualize_bounding_box_formats():
  plt.rc('font', family='AppleGothic')
  fig, axes = plt.subplots(1, 2, figsize=(12, 5))
  img = np.ones((300, 400, 3)) * 0.8

  x1, y1, x2, y2 = 50, 50, 200, 150

  axes[0].imshow(img)
  rect1 = patches.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=2, edgecolor='red', facecolor='none')
  axes[0].add_patch(rect1)
  axes[0].text(x1, y1-5, f'({x1}, {y1})', color='red', fontsize=10)
  axes[0].text(x2, y2+15, f'({x2}, {y2})', color='red', fontsize=10)
  axes[0].set_title('(x1, y1, x2, y2) 형식')
  axes[0].set_xlim(0, 400)
  axes[0].set_ylim(300, 0)

  plt.tight_layout()
  plt.show()

visualize_bounding_box_formats()