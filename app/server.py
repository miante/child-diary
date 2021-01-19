from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.api import routers
from app.api.auth.backend import SessionAuthBackend
from app.core import settings
from app.core.log import configure_logging

configure_logging()

app = FastAPI(
    debug=settings.DEBUG,
    title='Child Growth Diary',
    description='Child diary for tracking healthy lifestyle.',
    version=settings.VERSION,
)

# Middlewares
app.add_middleware(AuthenticationMiddleware, backend=SessionAuthBackend())
app.add_middleware(SessionMiddleware, secret_key=settings.secrets.SESSION_MIDDLEWARE_SECRET)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=['childdiary.info', '*.childdiary.info', '127.0.0.1'])

# Routing
app.include_router(routers.router, prefix='/api')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=80)
