"""Provides settings and related utilities for the application."""
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Provides application settings."""

    TITLE: str = "Health Universe - FastAPI 🚀"
    DESCRIPTION: str = "This template provides a starter FastAPI application for deployable to Health Universe."
    VERSION: str = "1"
    DEBUG: bool = True
    API_URL: str = "/api/v1"
    OPEN_API_URL: str = "/openapi.json"


@lru_cache()
def _get_settings() -> Settings:
    """Per the FastAPI docs, this function will cache the settings for the application.

    https://fastapi.tiangolo.com/advanced/settings/?h=settings#creating-the-settings-only-once-with-lru_cache

    Returns:
        The application settings.
    """
    return Settings()


settings = _get_settings()
