# Notebook
## _Small app on django_

## installation

- download a repository
- For installation of packages you can use the commands: 
```sh
pipenv install
```
After successfully installation all packages and framework, create database and superuser

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
after creation of the DB, fill him with the help a fill_db command (added 100 random users per run)
```sh
python manage.py fill_db
```
Open your browser and go to 
```sh 
http://localhost:8000/notebook/
```