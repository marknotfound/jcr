## Project Dependencies
* Python 3.11+
* `pipenv`

## Local Setup
1. Copy `.env.example` into a new file `.env`
```sh
cp .env.example .env
```
2. Modify `.env` variables with appropriate data. This file is git ignored.
3. `pipenv install` to install dependencies
4. `pipenv shell` to enter a virtual environment shell
5. Run the local server with `python ./jcr/manage.py runserver` if you need it. Hint: you probably don't!

## Tests
To run unit tests from the root directory:
```
sh run_tests.sh
```

## Running the Web App
Make sure you followed the `Local Setup` section above. This app really only utilizes Django's ORM + management commands to work, but if you need to run the web server locally for some reason:
```sh
pipenv run ./jcr/manage.py migrate
pipenv run ./jcr/manage.py runserver
```
