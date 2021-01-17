from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.api import routers
from app.core import settings


app = FastAPI(
    debug=settings.DEBUG,
    title='Child Growth Diary',
    description='Child diary for tracking healthy lifestyle.',
    version=settings.VERSION,
)

# Middlewares
app.add_middleware(SessionMiddleware, secret_key=settings.secrets.SESSION_MIDDLEWARE_SECRET)

# Routing
app.include_router(routers.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=80)
