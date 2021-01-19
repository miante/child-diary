from fastapi import APIRouter

from .v1.auth.views import router as v1_auth_router
from .v1.body_index.views import router as v1_body_index_router
from .v1.child.views import router as v1_child_router
from .v1.homepage.views import router as v1_homepage_router
from .v1.users.views import router as v1_users_router


router = APIRouter()

router.include_router(v1_auth_router, tags=['auth'])
router.include_router(v1_body_index_router, tags=['body-index'])
router.include_router(v1_child_router, tags=['child'])
router.include_router(v1_homepage_router, tags=['homepage'])
router.include_router(v1_users_router, tags=['users'])
