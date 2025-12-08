from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: dict):
    return item 

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}