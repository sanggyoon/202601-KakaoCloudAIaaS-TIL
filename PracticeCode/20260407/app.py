from fastapi import FastAPI
from pydantic import BaseModel
import pytesseract
import cv2
import os

app = FastAPI()

IMAGES_DIR = "/images"

@app.get("/images")
def list_images():
    files = [
        f for f in os.listdir(IMAGES_DIR)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))
    ]
    return {"images": files}

class OCRRequest(BaseModel):
    filename: str
    lang: str

@app.post("/ocr")
def perform_ocr(req: OCRRequest):
    image_path = f"{IMAGES_DIR}/{req.filename}"
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "이미지를 읽을 수 없습니다."}
    text = pytesseract.image_to_string(image, lang=req.lang)
    return {"text": text}
