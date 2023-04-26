#!/bin/sh
cd jcr
pipenv run ./manage.py test
cd ..