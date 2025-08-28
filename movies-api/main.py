import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(
    title="Movies Catalog",
)


@app.get("/")
def read_root(request: Request):
    docs_url = request.url.replace(path="/docs", query="")
    return {"message": "Hello! This my app", "docs": str(docs_url)}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
