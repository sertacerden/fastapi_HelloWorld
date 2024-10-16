from fastapi import FastAPI
from fastapi import Query, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    age: int

app = FastAPI()

@app.get("/helloworld")
def show_msg(
    name: str = Query("World", description="Enter your name to display your name. Otherwise the code will print Hello World")):
    return {
        "message": "Hello {}".format(name),
    }
async def create_item(item: Item):
    return item
