# labasi

a python/django based version of cfdb

## Install

1. clone the repo
2. create a virtual environment and run install the required packages `pip install > requirements`
3. adapt default.env to your needs and run `set_env_varibales.sh` (or copy default.env to secret.env if you use other db-credentials than the postgres default ones; make sure to adapt `set_env_varibales.sh` to your needs)
3. makemigrations and migrate `python manage.py makemigrations`and `python manage.py migrate`
4. start the dev-server `python manage.py runserver`
5. browse to http://127.0.0.1:8000/

