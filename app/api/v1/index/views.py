from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core import settings

router = APIRouter()


@router.get('/')
def index(requset: Request):
    body = """
        <!doctype html>
        <html lang="en">
           <head>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
              <title>Child Growth Diary</title>
              <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
              integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
           </head>
           <body>
              <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow">
                 <h5 class="my-0 mr-md-auto font-weight-normal">v{version}</h5>
                <nav class="my-2 my-md-0 mr-md-3">
                    <a class="p-2 text-dark" href="{base_url}redoc">Redoc</a>
                    <a class="p-2 text-dark" href="{base_url}docs">Swagger</a>
                  </nav>
                 {auth_btn}
              </div>
              <div class="px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
                 <h1 class="display-4">Child Growth Diary</h1>
                 <p class="lead">Child diary for tracking healthy lifestyle.</p>
                 {user_msg}
              </div>
           </body>
        </html>
    """

    user = requset.session.get('user')

    auth_btn = '<a class="btn btn-outline-success" href="{base_url}login">Sign in</a>'
    user_message = ''
    if user:
        auth_btn = '<a class="btn btn-outline-danger" href="{base_url}logout">Logout</a>'
        user_message = """<br><br><hr><p>You logged in as <h5>{user}</h5></p>""".format(user=user['email'])
    auth_btn = auth_btn.format(base_url=requset.base_url)

    formatted_body = body.format(
        base_url=requset.base_url,
        user_msg=user_message,
        auth_btn=auth_btn,
        version=settings.VERSION,
    )

    return HTMLResponse(formatted_body)
