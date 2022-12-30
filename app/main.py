from fastapi import FastAPI
from mangum import Mangum

from app.api.api_router_v1 import api_router

app = FastAPI(title="CheckNolNol API")
app.include_router(router=api_router, prefix="/api/v1")


@app.get("/")
async def hello():
    return "hello world!"


handler = Mangum(app=app)
