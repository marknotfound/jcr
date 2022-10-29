#!/usr/bin/env sh
python /app/jcr/manage.py migrate
python /app/jcr/manage.py notify_discord