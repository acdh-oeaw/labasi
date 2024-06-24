# labasi

a python/django based version of cfdb

## Install
The application was build with Python 3.4.

1. clone the repo
2. create a virtual environment and run install the required packages `pip install > requirements`
3. makemigrations and migrate `python manage.py makemigrations`and `python manage.py migrate`
4. start the dev-server `python manage.py runserver`
5. browse to http://127.0.0.1:8000/

## Upload the data
To ingest some sample data (found in data-directory), you have to execute the ipython scripts
 
* `importSigns.ipynb`,
* `importTablets.ipynb`, 
* `importGlyphs.ipynb`. 

To do so

1. Start a new iypthon session `python manage.py shell_plus --notebook`.
2. Open e.g. `importSigns.ipynb`.
3. Execute the script cell by cell. 
4. Repeat this with the two remaining scripts. 