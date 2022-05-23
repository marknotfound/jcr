import os
from .base import *

def update_environment():
    with open(BASE_DIR / ".." / ".env") as env_file:
        for line in env_file:
            (key, _, value) = line.partition("=")
            os.environ.update({key: value})

update_environment()

SECRET_KEY = 'django-insecure-s0+o81*#a%1v-4kq8)j9$=c$r8ya2=jaj1yqq7g!6%-1*7udzq'

ALLOWED_HOSTS = ["*"]

NYRR_WEBHOOK = os.environ.get("NYRR_WEBHOOK", NYRR_WEBHOOK)
