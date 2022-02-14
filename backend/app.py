
# IMPORT STANDARD LIBRARIES
import os
import datetime

# IMPORT THIRD PARTY LIBRARIES
from fastapi import FastAPI


app = FastAPI(title="AwsTestApp")


@app.get("/")
def root():
    return "Test App Root"


@app.get("/ping")
def ping():
    return {"reply": "Hello!", "time": datetime.datetime.utcnow().isoformat()}


@app.get("/value")
def get_value():
    return {"value": 5}


@app.put("/value/{value}")
def set_value(value: int):
    return {"updated value": value}
