from fastapi import FastAPI

api = FastAPI()


@api.get("/api/v1/root")
def root():
    return {
        "status": True,
        "data": "Welcome to FastApi Crypto Predictor"
    }

def get_something():
    return "Something"

def another_get():
    return "Jus for fun"