FROM python:3.10.8-slim-buster

RUN set +x && \
  pip install pipenv && \
  mkdir /app

WORKDIR /app
COPY . /app

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "/app/jcr/manage.py", "schedule_scrape"]