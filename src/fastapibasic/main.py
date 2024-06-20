from fastapi import FastAPI
from .routes import router as main_router
from .prometheus import prometheus_middleware, metrics


def load_description(file_path: str) -> str:
    """
    Load the API description from a Markdown file.

    Parameters
    ----------
    file_path : str
        The path to the Markdown file

    Returns
    -------
    str
        The content of the Markdown file as a string
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


description = load_description('docs.md')

app = FastAPI(
    title="Basic Api FrameWork",
    description=description,
    version="0.0.1",
)

# Include Prometheus middleware
app.middleware("http")(prometheus_middleware)

# Include Prometheus metrics endpoint
app.add_route("/metrics", metrics, methods=["GET"], include_in_schema=False)

app.include_router(main_router)
