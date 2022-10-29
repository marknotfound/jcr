FROM python:3.10.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN set +x && \
  apt update && \
  apt install -y cron && \
  pip install pipenv && \
  mkdir /app

RUN (crontab -l; echo "0 * * * * python /app/jcr/manage.py scrape_races") | crontab -

WORKDIR /app
COPY . /app

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["gunicorn", "--chdir", "/app/jcr", "jcr.wsgi"]