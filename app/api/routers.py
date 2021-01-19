from fastapi import APIRouter

from .auth.views import router as auth_router
from .v1.index.views import router as v1_index_router


router = APIRouter()

router.include_router(auth_router, tags=['auth'])
router.include_router(v1_index_router, tags=['index'])
