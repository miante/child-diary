from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.core import settings


router = APIRouter()


@router.get('/')
def index():
    """
    Returns the status, version of API
    """

    return JSONResponse({'version': settings.VERSION})
