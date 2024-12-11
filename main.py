from fastapi import FastAPI

app = FastAPI()

# 以下のコードを追加する
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None): # 第二引数にqを設定する
    return {"item_id": item_id, "q": q}