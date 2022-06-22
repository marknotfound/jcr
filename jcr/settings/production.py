import os
import re
from .base import *

def _postgres_url_to_config(database_url):
    match = re.match(r'postgres://(.+):(.+)@(.+):(.+)/(.+)', database_url)
    (user, password, host, port, dbname) = match.groups()

    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dbname,
        'USER': user,
        'PASSWORD': password,
        'HOST': host,
        'PORT': port,
    }

DEBUG = False

ALLOWED_HOSTS = ["*"]

NYRR_WEBHOOK = os.environ["NYRR_WEBHOOK"]

# Database
DATABASES = {
    'default': _postgres_url_to_config(os.environ["DATABASE_URL"])
}


LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "WARN"
    }
}