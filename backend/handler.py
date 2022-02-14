# IMPORT STANDARD LIBRARIES
import os
import datetime

# IMPORT THIRD PARTY LIBRARIES
from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
def root():
    return "API ROOT! 5"


@app.get("/ping")
def ping():
    return {"reply": "Hello NEW", "time": datetime.datetime.utcnow().isoformat()}


@app.get("/value/")
def get_value():
    return "value: 4"


@app.put("/value/")
def set_value(value):
    return f"new value: {value}"


handler = Mangum(app)
