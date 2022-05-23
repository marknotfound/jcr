from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

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