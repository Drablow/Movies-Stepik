import logging
import uvicorn

from fastapi import FastAPI, Request

from api import router as api_router

from core import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
)

app = FastAPI(
    title="Movies Catalog",
)

app.include_router(api_router)


@app.get("/")
def read_root(request: Request):
    docs_url = request.url.replace(path="/docs", query="")
    return {"message": "Hello! This my app", "docs": str(docs_url)}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
