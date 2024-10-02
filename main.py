from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

@app.get("/helloworld")
def show_msg(name: str = Query("World", description="Enter your name to display your name. Otherwise the code will print Hello World")):
    return {
        "message": "Hello {}".format(name)
    }
