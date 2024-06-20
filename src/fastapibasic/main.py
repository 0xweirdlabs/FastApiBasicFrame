from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = FastAPI()

# Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response

@app.get("/metrics", include_in_schema=False)
async def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# default routes
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)