"""Provides schemas for API health checks and other various diagnostics."""
from pydantic import BaseModel


class HealthCheckSchema(BaseModel):
    """Simple schema for a health check."""

    ping: str


class ExceptionMessage(BaseModel):
    """Exception message for custom error responses."""

    detail: str
