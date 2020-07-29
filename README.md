# Readme

> REST API created by Django and Neo4j.

## Build Setup

``` bash
# create virtual environement
pip install virtualenv
virtualenv env
env\Scripts\activate

# install requirements
pip install -r requirements.txt

# for add new requirements 
pip freeze > requirements.txt

# create constraintes
python manage.py install_labels 

# run api server
python manage.py runserver

# open Django shell 
python manage.py shell
```
