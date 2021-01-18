apt update
apt -y install python3-virtualenv
virtualenv venv
source venv/bin/activate
gunicorn app.server:app --bind=0.0.0.0:80 -w 5 -k uvicorn.workers.UvicornWorker --daemon --reload
