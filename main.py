from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"endpoints": ["/get_milk"]}

@app.get("/get_milk", status_code=418)
async def get_milk():
    return {"ok": False, "status": 418, "message": "Out of milk"}