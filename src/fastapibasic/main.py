from fastapi import FastAPI
from .routes import router as main_router
from .prometheus import prometheus_middleware, metrics

app = FastAPI()

# Include Prometheus middleware
app.middleware("http")(prometheus_middleware)

# Include Prometheus metrics endpoint
app.add_route("/metrics", metrics, methods=["GET"], include_in_schema=False)

app.include_router(main_router)
