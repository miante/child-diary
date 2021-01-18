apt update
apt -y install python3-virtualenv
virtualenv venv
source venv/bin/activate
gunicorn app.server:app --bind=0.0.0.0:80 -w 5 -k uvicorn.workers.UvicornWorker --daemon --reload



export =

    'username': settings.POSTGRES_USERNAME,
    'password': settings.POSTGRES_PASSWORD,
    'host': settings.POSTGRES_HOST,
    'port': settings.POSTGRES_PORT,
    'name': settings.POSTGRES_DATABASE,