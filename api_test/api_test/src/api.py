from fastapi import FastAPI
from src.test import Adder
from fastapi.middleware.cors import CORSMiddleware
# from src.endpoints import ingest, test
# from src.parametric.find_location import Find
# from src.util.settings import *
import faulthandler 
import json

# initialize fast api
app = FastAPI(title= "Parametric Piecewise")
faulthandler.enable()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    adder = Adder()
    resources = {
        "Title": "Ebenezer's Application",
        "Count": adder.count
    }
    return resources

@app.get("/awesome")
def awesome():
    resources = {
        "Title": "Ebenezer's Application 2 Demo"
    }
    return resources
