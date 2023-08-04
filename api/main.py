from fastapi import FastAPI

app= FastAPI()


@app.get("/")
def raiz():
    return{"Hello": "Hola"}

@app.get("/items/{item_id}/{m}")
def read_items(item_id:int,m:str=None):
    return {"item_id": item_id,"m":m}