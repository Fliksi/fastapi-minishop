from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в мини-магазин на FastAPI!"}
