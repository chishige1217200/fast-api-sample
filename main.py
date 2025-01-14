from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path
import delaytask

app = FastAPI()

# 画像を保存するディレクトリ
UPLOAD_DIR = Path("uploaded_images")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/delay")
async def delay():
    delaytask.run_task()
    return {"Hello": "Delay"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None): # 第二引数にqを設定する
    return {"item_id": item_id, "q": q}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """
    画像ファイルをアップロードし、サーバーに保存するエンドポイント
    """
    # ファイルの拡張子を確認
    if not file.content_type.startswith("image/"):
        return {"error": "アップロードされたファイルは画像ではありません。"}

    # 保存するファイルパスを指定
    file_path = UPLOAD_DIR / file.filename

    # ファイルを保存
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "file_path": str(file_path)}
