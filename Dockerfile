FROM python:3.10.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN set +x && \
  apt update && \
  apt install -y cron && \
  pip install pipenv && \
  mkdir /app

WORKDIR /app
COPY . /app

RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

CMD ["sh", "/app/run_prod.sh"]
