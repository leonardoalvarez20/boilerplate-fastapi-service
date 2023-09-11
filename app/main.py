from fastapi import FastAPI

from app.healthcheck.api.router import healthcheck_router


def init():
    """
    Initialize the app:
    - Configure FastAPI app
    - Configure the healthcheck route
    - Configure routing path for v1 endpoints
    """
    _app = FastAPI(
        title="fastapi-boilerplate",
        description="Boilerplate allow to create services with a base code",
        version="0.1.0"
    )

    _app.include_router(healthcheck_router)

    return _app


app = init()
