from PIL import Image, ImageDraw, ImageFilter
import io
import cv2
import numpy as np
from segment_anything import sam_model_registry, SamPredictor
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(page_title='배경 합성 도구', layout='wide')
st.title('배경 합성 도구')

# ── 세션 키 초기화 ───────────────────────────────────────────
DEFAULTS = {
  # SAM
  'sam_points': [], 'sam_labels': [], 'sam_image': None,
  'sam_image_np': None, 'sam_result': None, 'sam_bg': None,
  # GrabCut
  'gc_image': None, 'gc_image_np': None, 'gc_result': None,
}
for key, val in DEFAULTS.items():
  if key not in st.session_state:
    st.session_state[key] = val


# ── 공통 유틸 ────────────────────────────────────────────────
def to_png_bytes(image: Image.Image) -> bytes:
  buf = io.BytesIO()
  image.save(buf, format='PNG')
  return buf.getvalue()


def composite(fg_rgba: Image.Image, bg: Image.Image) -> Image.Image:
  bg_r = bg.convert('RGBA').resize(fg_rgba.size, Image.LANCZOS)
  out = bg_r.copy()
  out.paste(fg_rgba, mask=fg_rgba.split()[3])
  return out


# ── SAM 관련 ─────────────────────────────────────────────────
@st.cache_resource
def load_sam():
  sam = sam_model_registry['vit_b'](checkpoint='sam_vit_b_01ec64.pth')
  sam.to(device='cpu')
  return SamPredictor(sam)


def draw_points(image, points, labels):
  img = image.copy()
  draw = ImageDraw.Draw(img)
  for (x, y), label in zip(points, labels):
    color = (0, 220, 0) if label == 1 else (220, 0, 0)
    draw.ellipse([x-9, y-9, x+9, y+9], fill=color, outline='white', width=2)
    draw.text((x+12, y-8), '전경' if label == 1 else '배경', fill=color)
  return img


def pil_apply_filters(image: Image.Image, gaussian_r: float, median_s: int) -> Image.Image:
  img = image.copy()
  if gaussian_r > 0:
    img = img.filter(ImageFilter.GaussianBlur(radius=gaussian_r))
  if median_s > 1:
    s = median_s if median_s % 2 == 1 else median_s + 1
    img = img.filter(ImageFilter.MedianFilter(size=s))
  return img


def make_transparent_pil(image_np: np.ndarray, mask: np.ndarray) -> Image.Image:
  rgba = np.dstack([image_np, np.zeros(image_np.shape[:2], dtype=np.uint8)])
  rgba[mask, 3] = 255
  return Image.fromarray(rgba, 'RGBA')


# ── GrabCut 관련 ─────────────────────────────────────────────
def run_grabcut(image_np: np.ndarray, margin: int, iterations: int) -> Image.Image:
  img_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
  h, w = img_bgr.shape[:2]
  mask = np.zeros((h, w), np.uint8)
  rect = (margin, margin, w - margin * 2, h - margin * 2)
  bgd = np.zeros((1, 65), np.float64)
  fgd = np.zeros((1, 65), np.float64)
  cv2.grabCut(img_bgr, mask, rect, bgd, fgd, iterations, cv2.GC_INIT_WITH_RECT)
  mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
  rgba = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2BGRA)
  rgba[:, :, 3] = mask2 * 255
  return Image.fromarray(cv2.cvtColor(rgba, cv2.COLOR_BGRA2RGBA), 'RGBA')


# ── 후처리 관련 ──────────────────────────────────────────────
def smooth_alpha(image_rgba: Image.Image, kernel: int) -> Image.Image:
  arr = np.array(image_rgba)
  alpha = arr[:, :, 3].astype(np.float32)
  k = kernel if kernel % 2 == 1 else kernel + 1
  blurred = cv2.GaussianBlur(alpha, (k, k), 0)
  out = arr.copy()
  out[:, :, 3] = blurred.astype(np.uint8)
  return Image.fromarray(out, 'RGBA')


def adjust_transparency(image_rgba: Image.Image, factor: float) -> Image.Image:
  arr = np.array(image_rgba).copy()
  arr[:, :, 3] = np.clip(arr[:, :, 3].astype(np.float32) * factor, 0, 255).astype(np.uint8)
  return Image.fromarray(arr, 'RGBA')


# ════════════════════════════════════════════════════════════
# 탭 구성
# ════════════════════════════════════════════════════════════
tab_sam, tab_gc, tab_filter, tab_post = st.tabs(['SAM 세그멘테이션', 'GrabCut 배경 제거', '이미지 필터', '후처리'])


# ────────────────────────────────────────────────────────────
# TAB 1 · SAM 세그멘테이션
# ────────────────────────────────────────────────────────────
with tab_sam:
  with st.sidebar:
    st.header('SAM 설정')
    label_type = st.radio('클릭 유형', ['전경 (객체)', '배경'], index=0)
    label_value = 1 if '전경' in label_type else 0

    st.divider()
    st.subheader('① 원본 이미지')
    sam_src = st.file_uploader('원본 사진', type=['jpg', 'jpeg', 'png'], key='sam_src')

    st.divider()
    st.subheader('② 배경 이미지')
    sam_bg_file = st.file_uploader('배경 사진', type=['jpg', 'jpeg', 'png'], key='sam_bg_up')
    if sam_bg_file:
      st.session_state.sam_bg = Image.open(sam_bg_file).convert('RGB')
    if st.session_state.sam_bg:
      st.image(st.session_state.sam_bg, caption='선택된 배경', use_container_width=True)
      if st.button('배경 제거', key='rm_bg'):
        st.session_state.sam_bg = None
        st.rerun()

    st.divider()
    if st.button('포인트 초기화', use_container_width=True):
      st.session_state.sam_points = []
      st.session_state.sam_labels = []
      st.session_state.sam_result = None
      st.rerun()

    if st.session_state.sam_points:
      st.write(f'포인트 수: **{len(st.session_state.sam_points)}개**')
      for i, ((x, y), l) in enumerate(zip(st.session_state.sam_points, st.session_state.sam_labels)):
        st.write(f'{i+1}. {"🟢 전경" if l==1 else "🔴 배경"} ({x}, {y})')

  # 원본 이미지 로드
  if sam_src:
    img = Image.open(sam_src).convert('RGB')
    prev = st.session_state.sam_image_np
    if prev is None or img.size != Image.fromarray(prev).size:
      st.session_state.sam_image = img
      st.session_state.sam_image_np = np.array(img)
      st.session_state.sam_points = []
      st.session_state.sam_labels = []
      st.session_state.sam_result = None

  if st.session_state.sam_image is None:
    st.info('사이드바에서 원본 이미지를 업로드하세요.')
    st.stop()

  col_l, col_r = st.columns(2)

  with col_l:
    st.subheader('원본 이미지')
    st.caption('클릭하여 전경/배경 포인트 지정')
    display = draw_points(st.session_state.sam_image, st.session_state.sam_points, st.session_state.sam_labels)
    coords = streamlit_image_coordinates(display, key='sam_click')
    if coords:
      x, y = coords['x'], coords['y']
      last = st.session_state.sam_points[-1] if st.session_state.sam_points else None
      if last != (x, y):
        st.session_state.sam_points.append((x, y))
        st.session_state.sam_labels.append(label_value)
        st.rerun()

  with col_r:
    st.subheader('결과')
    if not st.session_state.sam_points:
      st.info('왼쪽 이미지를 클릭하여 포인트를 지정하세요.')
    else:
      if st.button('세그멘테이션 실행', use_container_width=True, type='primary'):
        with st.spinner('분석 중...'):
          predictor = load_sam()
          predictor.set_image(st.session_state.sam_image_np)
          masks, scores, _ = predictor.predict(
            point_coords=np.array(st.session_state.sam_points),
            point_labels=np.array(st.session_state.sam_labels),
            multimask_output=True,
          )
          best = masks[np.argmax(scores)]
          st.session_state.sam_result = (masks, scores, best)

      if st.session_state.sam_result:
        masks, scores, best = st.session_state.sam_result
        transparent = make_transparent_pil(st.session_state.sam_image_np, best)
        st.success(f'신뢰도: {scores.max():.1%}')

        if st.session_state.sam_bg:
          composited = composite(transparent, st.session_state.sam_bg)
          st.image(composited, caption='배경 합성 결과', use_container_width=True)
          st.download_button('합성 이미지 다운로드', to_png_bytes(composited),
                             'composited.png', 'image/png', use_container_width=True)
        else:
          st.image(transparent, caption='투명 배경', use_container_width=True)
          st.warning('사이드바에서 배경 사진을 선택하면 합성 결과를 볼 수 있습니다.')

        st.download_button('투명 배경 PNG 다운로드', to_png_bytes(transparent),
                           'transparent.png', 'image/png', use_container_width=True)

        with st.expander('마스크 후보 보기'):
          cols = st.columns(3)
          for i, (m, s) in enumerate(zip(masks, scores)):
            ov = (st.session_state.sam_image_np * (1 - 0.6 * m[:,:,None]) +
                  np.array([0, 140, 255]) * 0.6 * m[:,:,None]).astype(np.uint8)
            cols[i].image(ov, caption=f'{s:.3f}', use_container_width=True)


# ────────────────────────────────────────────────────────────
# TAB 2 · GrabCut 배경 제거
# ────────────────────────────────────────────────────────────
with tab_gc:
  st.subheader('GrabCut 배경 제거')
  st.caption('GrabCut 알고리즘으로 전경 객체를 자동으로 분리합니다.')

  gc_col_ctrl, gc_col_view = st.columns([1, 2])

  with gc_col_ctrl:
    gc_file = st.file_uploader('이미지 업로드', type=['jpg', 'jpeg', 'png'], key='gc_up')
    if gc_file:
      gc_img = Image.open(gc_file).convert('RGB')
      if (st.session_state.gc_image_np is None or
          gc_img.size != Image.fromarray(st.session_state.gc_image_np).size):
        st.session_state.gc_image = gc_img
        st.session_state.gc_image_np = np.array(gc_img)
        st.session_state.gc_result = None

    st.divider()
    margin = st.slider('테두리 여백(px)', 10, 150, 50, 5,
                       help='이미지 가장자리에서 배경으로 처리할 픽셀 수')
    iterations = st.slider('반복 횟수', 1, 10, 5,
                           help='값이 클수록 정밀하지만 느립니다')

    gc_bg_file = st.file_uploader('합성할 배경 사진 (선택)', type=['jpg', 'jpeg', 'png'], key='gc_bg_up')
    gc_bg = Image.open(gc_bg_file).convert('RGB') if gc_bg_file else None

    st.divider()
    run_gc = st.button('GrabCut 실행', use_container_width=True, type='primary',
                       disabled=st.session_state.gc_image is None)

  with gc_col_view:
    if st.session_state.gc_image is None:
      st.info('왼쪽에서 이미지를 업로드하세요.')
    else:
      if run_gc:
        with st.spinner('GrabCut 실행 중...'):
          st.session_state.gc_result = run_grabcut(
            st.session_state.gc_image_np, margin, iterations)

      st.image(st.session_state.gc_image, caption='원본', use_container_width=True)

      if st.session_state.gc_result:
        transparent_gc = st.session_state.gc_result
        st.divider()

        if gc_bg:
          composited_gc = composite(transparent_gc, gc_bg)
          st.image(composited_gc, caption='배경 합성 결과', use_container_width=True)
          st.download_button('합성 이미지 다운로드', to_png_bytes(composited_gc),
                             'gc_composited.png', 'image/png', use_container_width=True)
        else:
          st.image(transparent_gc, caption='투명 배경 결과', use_container_width=True)

        st.download_button('투명 배경 PNG 다운로드', to_png_bytes(transparent_gc),
                           'gc_transparent.png', 'image/png', use_container_width=True)


# ────────────────────────────────────────────────────────────
# TAB 3 · 이미지 필터
# ────────────────────────────────────────────────────────────
with tab_filter:
  st.subheader('이미지 필터')
  st.caption('가우시안 블러와 메디안 필터를 적용하여 이미지를 보정합니다.')

  flt_col_ctrl, flt_col_view = st.columns([1, 2])

  with flt_col_ctrl:
    flt_file = st.file_uploader('이미지 업로드', type=['jpg', 'jpeg', 'png'], key='flt_up')

    st.divider()
    st.markdown('**가우시안 블러**')
    gauss_r = st.slider('블러 강도', 0.0, 20.0, 0.0, 0.5,
                        key='flt_gauss', help='0이면 비활성. 값이 클수록 흐려짐')

    st.divider()
    st.markdown('**메디안 필터**')
    median_s = st.slider('필터 크기', 1, 21, 1, 2,
                         key='flt_median', help='1이면 비활성. 노이즈 제거에 효과적 (홀수만 유효)')

  with flt_col_view:
    if flt_file is None:
      st.info('왼쪽에서 이미지를 업로드하세요.')
    else:
      flt_image = Image.open(flt_file).convert('RGB')
      filtered = pil_apply_filters(flt_image, gauss_r, median_s)

      col_orig, col_filt = st.columns(2)
      with col_orig:
        st.image(flt_image, caption='원본', use_container_width=True)
      with col_filt:
        label = f'필터 적용 (블러={gauss_r}, 메디안={median_s})'
        st.image(filtered, caption=label, use_container_width=True)

      st.download_button('필터 적용 이미지 다운로드', to_png_bytes(filtered),
                         'filtered.png', 'image/png', use_container_width=True)


# ────────────────────────────────────────────────────────────
# TAB 4 · 후처리
# ────────────────────────────────────────────────────────────
with tab_post:
  st.subheader('후처리')
  st.caption('투명 PNG의 알파 채널을 보정하고 전체 투명도를 조절합니다.')

  post_col_ctrl, post_col_view = st.columns([1, 2])

  with post_col_ctrl:
    post_file = st.file_uploader('투명 PNG 업로드 (RGBA)', type=['png'], key='post_up')

    st.divider()
    st.markdown('**1. 마스크 경계 부드럽게 (알파 블러)**')
    blur_k = st.slider('블러 커널 크기', 1, 51, 5, 2,
                       help='1이면 비활성. 값이 클수록 경계가 부드러워짐 (홀수만 유효)')

    st.divider()
    st.markdown('**2. 전체 투명도 조절**')
    trans_factor = st.slider('투명도 배율', 0.0, 1.0, 1.0, 0.05,
                             help='1.0이면 원본 유지, 낮을수록 반투명')

    post_bg_file = st.file_uploader('합성할 배경 사진 (선택)', type=['jpg', 'jpeg', 'png'], key='post_bg_up')
    post_bg = Image.open(post_bg_file).convert('RGB') if post_bg_file else None

  with post_col_view:
    if post_file is None:
      st.info('왼쪽에서 투명 PNG를 업로드하세요.')
    else:
      src_rgba = Image.open(post_file).convert('RGBA')
      st.image(src_rgba, caption='원본 (RGBA)', use_container_width=True)

      # 후처리 적용
      processed = smooth_alpha(src_rgba, blur_k)
      processed = adjust_transparency(processed, trans_factor)

      st.divider()
      st.markdown('**후처리 결과**')

      if post_bg:
        composited_post = composite(processed, post_bg)
        st.image(composited_post, caption='배경 합성 결과', use_container_width=True)
        st.download_button('합성 이미지 다운로드', to_png_bytes(composited_post),
                           'post_composited.png', 'image/png', use_container_width=True)
      else:
        st.image(processed, caption='후처리 결과', use_container_width=True)

      st.download_button('후처리 PNG 다운로드', to_png_bytes(processed),
                         'post_processed.png', 'image/png', use_container_width=True)
