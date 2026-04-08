from fastapi import FastAPI
import fastapi

# Print FastAPI version
print("FastAPI 버전: " + fastapi.__version__)

# FastAPI 앱 생성 (카페 오픈!)
app = FastAPI()

# 첫 번째 엔드포인트 (기본 메뉴)
@app.get("/")
def read_root():
    return {"message": "안녕하세요! FastAPI 카페입니다!"}

# 인사 엔드포인트
@app.get("/hello")
def say_hello():
    return {"greeting": "Hello World!", "cafe": "FastAPI Coffee Shop", "message": "Hello world!"}

@app.post("/items")
def create_item():
    return {"message": "item!"}