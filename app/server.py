from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.core.configs import settings

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=settings.secrets.SESSION_MIDDLEWARE_SECRET)


# @app.route("/")
# async def homepage(request: Request):
#     user = request.session.get("user")
#     if user:
#         data = json.dumps(user)
#         html = (
#             f"<pre>{data}</pre>"
#             '<a href="/logout">logout</a>'
#         )
#         return HTMLResponse(html)
#     return HTMLResponse('<a href="/login">login</a>')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=80)
