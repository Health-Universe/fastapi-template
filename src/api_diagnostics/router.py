"""Provides routes for API health checks and other various diagnostics."""
from fastapi import APIRouter

from src.api_diagnostics.schemas import HealthCheckSchema

router = APIRouter()


@router.get("/healthcheck", include_in_schema=False)
async def _healthcheck() -> HealthCheckSchema:
    return HealthCheckSchema(ping="ok")
