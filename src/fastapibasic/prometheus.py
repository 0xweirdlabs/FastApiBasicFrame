from fastapi import Request
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

# Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests")
HTTP_STATUS_COUNTER = Counter("http_status_count", "Count of HTTP status codes", ["status_code"])


async def prometheus_middleware(request: Request, call_next):
    """
    Middleware to track Prometheus metrics for each request.

    Parameters
    ----------
    request : Request
        The incoming request
    call_next : function
        The next middleware or route handler

    Returns
    -------
    Response
        The response generated by the next middleware or route handler
    """
    REQUEST_COUNT.inc()
    response = await call_next(request)
    status_code = str(response.status_code)
    HTTP_STATUS_COUNTER.labels(status_code=status_code).inc()
    return response


async def metrics(request: Request):
    """
    Endpoint to expose Prometheus metrics.

    Parameters
    ----------
    request : Request
        The incoming request

    Returns
    -------
    PlainTextResponse
        The response containing the metrics in text format
    """
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
