# Stock_Image

### Python/Django/Django Rest Framework

###(Create a virtual env if none exists) virtualenv --python=python3 venv
###(Activate env) source venv/bin/activate
###(Save dependencies to txt file) pip install <package> && pip freeze > requirements.txt
###(Start project) django-admin.py startproject <project>
###(Start App) django-admin.py startapp <app> 
###(Make model migrations to db) python manage.py makemigrations
###(Migrate to DB) python manage.py migrate
###Need to add rest_framework and app name to settings.py


# Framework notes

###Models - Make relationships and define tables in db
###Serializers - Convert to JSON and list what fields need to be returned for models
###Views - Define query sets and serializers for each model
###Urls - register views with router