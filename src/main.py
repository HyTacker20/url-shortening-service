from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/shorten/{shorten_url}")
def get_original_url(shorten_url: str):
    return
