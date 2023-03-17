#!/bin/sh
cd jcr
pipenv run ./manage.py test --settings settings.test
cd ..