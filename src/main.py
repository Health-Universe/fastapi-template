"""Contains the main FastAPI application object."""
import os
import time

from fastapi import FastAPI

from src.api_diagnostics.router import router as diagnostic_router
from src.api_diagnostics.schemas import ExceptionMessage
from src.chads_vasc_score.router import router as cvs_router
from src.config import settings

# It's good practice to set default server timezone to UTC for standardization.
os.environ["TZ"] = "UTC"
time.tzset()


app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    debug=settings.DEBUG,
    version=settings.VERSION,
    openapi_url=settings.OPEN_API_URL,
    swagger_ui_parameters={"persistAuthorization": True},
    responses={
        400: {"model": ExceptionMessage},
        401: {"model": ExceptionMessage},
        403: {"model": ExceptionMessage},
        404: {"model": ExceptionMessage},
        422: {"model": ExceptionMessage},
    },
)


app.include_router(diagnostic_router, tags=["Diagnostics"])
app.include_router(cvs_router, prefix=settings.API_URL, tags=["CHA₂DS₂-VASc"])
