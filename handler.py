# IMPORT STANDARD LIBRARIES
import os
import datetime

# IMPORT THIRD PARTY LIBRARIES
from fastapi import FastAPI
from mangum import Mangum


stage = os.environ.get('STAGE', None) or ""
openapi_prefix = f"/{stage}"


app = FastAPI(title="MyAwesomeApp", openapi_prefix=openapi_prefix)


@app.get("/")
def root():
    return "API ROOT! 3"


@app.get("/hello")
def hello():
    return {"message": "Hello World edited"}


@app.get("/ping")
def ping():
    return {"reply": "Hello NEW", "time": datetime.datetime.utcnow().isoformat()}


@app.get("/api/{path}")
def api_test(path : str):
    return {
        "test": "Hey!",
        "path": path,
    }


handler = Mangum(app)
