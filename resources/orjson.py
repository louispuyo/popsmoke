from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from uvicorn import run
app = FastAPI()

@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]


if __name__ == "__main__":
    run(app)
    