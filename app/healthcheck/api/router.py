"""
Router for V1 version
"""
from fastapi import APIRouter

from app.healthcheck.api.v1 import endpoints as v1_endpoints

healthcheck_router = APIRouter()

healthcheck_router.include_router(
    router=v1_endpoints.router,
    prefix="/v1/healthcheck",
    tags=["Healthcheck"],
)
