from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get('/')
def index():
    return HTMLResponse("""
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
                 <h5 class="my-0 mr-md-auto font-weight-normal">Alfa version</h5>
              </div>
              <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
                 <h1 class="display-4">Child Growth Diary</h1>
                 <p class="lead">Child diary for tracking healthy lifestyle.</p>
              </div>
           </body>
        </html>
    """)
