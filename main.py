from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def hello(name: str = Query("World")):
    return {"message": f"Hello, {name}!"}
