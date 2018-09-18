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


> from customer.models import Choice, Question
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q = Question(question_text="What's up buddy?", pub_date=timezone.now())
>>> q.save()
>>> q = Question(question_text="What's up dude?", pub_date=timezone.now())
>>> q.save()


