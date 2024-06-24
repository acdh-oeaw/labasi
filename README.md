[![flake8 Lint](https://github.com/acdh-oeaw/labasi/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/labasi/actions/workflows/lint.yml)

# labasi

a python/django based version of cfdb

## Install

1. clone the repo
2. create a virtual environment and run install the required packages `pip install > requirements`
3. adapt default.env to your needs and run `set_env_varibales.sh` (or copy default.env to secret.env if you use other db-credentials than the postgres default ones; make sure to adapt `set_env_varibales.sh` to your needs)
3. makemigrations and migrate `python manage.py makemigrations`and `python manage.py migrate`
4. start the dev-server `python manage.py runserver`
5. browse to http://127.0.0.1:8000/




## Docker

At the ACDH-CH we use a centralized database-server. So instead of spawning a database for each service our services are talking to a database on this centralized db-server. This setup is reflected in the dockerized setting as well, meaning it expects an already existing database (either on your host, e.g. accessible via 'localhost' or some remote one)

### building the image

* `docker build -t labasi:latest .`
* `docker build -t labasi:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --rm --env-file docker.env --name labasi labasi:latest`