if [ "$INITIAL_COMMIT_DONE" != "true" ]; then
    apt update
    apt -y install python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    gunicorn app.server:app --bind=0.0.0.0:80 -w 5 -k uvicorn.workers.UvicornWorker --daemon --reload
    echo "INITIAL_COMMIT_DONE=true" >> ~/.bashrc
    source ~/.bashrc
else
  source venv/bin/activate
  pip install -U -r requirements.txt
fi
