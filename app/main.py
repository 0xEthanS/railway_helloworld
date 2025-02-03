from fastapi import FastAPI
from fastapi.responses import JSONResponse






app = FastAPI()



@app.get("/")
async def hello_world():
    return JSONResponse(
        content={
            "greeting": "Hello World!",
            "foo": "bar"
        },
        status_code=200
    )



