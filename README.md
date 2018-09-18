# python_django_app
Basic Python Django App

#Required DJango Important Command
mkdir pythonproject
cd pythonproject

#Install virtualend
pip install virtualenv

#create virtualend and actiavte
virtualenv envdev
cd envdev
cd Scripts
activate
cd ..

#Install django
pip install django

#Start django project
django-admin startproject MYSITE
python manage.py runserver 5000

#Start django project app
python manage.py startapp customer

#Migrate model
python manage.py makemigrations
python manage.py migrate

#create super admin user
python manage.py createsuperuser



