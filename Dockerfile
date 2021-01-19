FROM python:3.9

LABEL maintainer="max.seredenko@gmail.com"

ARG APP_DIR=/opt/child-growth-diary

RUN mkdir ${APP_DIR}
COPY ./requirements.txt ${APP_DIR}/requirements.txt

RUN pip install -r ${APP_DIR}/requirements.txt

COPY ./app/ ${APP_DIR}/app

# Finish image setup.
WORKDIR ${APP_DIR}

CMD ["gunicorn", "app.server:app", "--access-logfile '-'", "--error-logfile '-'", "--bind=0.0.0.0:8000", "-k uvicorn.workers.UvicornH11Worker", "--workers=5"]
