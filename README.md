# python_django_app
Basic Python Django App

#Required DJango Important Command
mkdir pythonproject
cd pythonproject
pip install virtualenv
virtualenv envdev
cd envdev
cd Scripts
activate
cd ..
pip install django
django-admin startproject MYSITE
python manage.py runserver 5000
python manage.py startapp customer
python manage.py migrate
python manage.py createsuperuser



