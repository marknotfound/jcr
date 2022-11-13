#!/bin/sh

set -e
mkdir -p /app/var/log
crontab /app/etc/crontab
cron

gunicorn --bind :8000 --chdir /app/jcr jcr.wsgi
