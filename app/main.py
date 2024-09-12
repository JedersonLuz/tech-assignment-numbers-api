from fastapi import FastAPI

from .routers import math

app = FastAPI()


app.include_router(math.router)


@app.get("/")
async def health_check():
    return {"status": "ok"}
