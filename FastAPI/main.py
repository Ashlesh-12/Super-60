import MultipleRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(MultipleRouter.router)

@app.get("/")
async def read_root():
    return {"Hello":"World"}