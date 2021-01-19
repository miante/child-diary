from fastapi import APIRouter
from pydantic.main import BaseModel

from app.core import settings


router = APIRouter()


class IndexResponse(BaseModel):
    version: str


@router.get('/', summary="Homepage", response_model=IndexResponse)
def homepage():
    """
    Returns the version of current API
    """

    return IndexResponse(version=settings.VERSION)
