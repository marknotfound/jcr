## Project Dependencies
* Python 3.10+
* `pipenv`

## Run Locally
1. Copy `.env.example` into a new file `.env`
```
$ cp .env.example .env
```
2. Modify `.env` variables with appropriate data. This file is git ignored.
3. `pipenv install` to install dependencies
4. `pipenv shell` to enter a virtual environment shell
5. Run the local server with `python ./jcr/manage.py runserver` if you need it. Hint: you probably don't!
