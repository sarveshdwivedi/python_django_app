# python_django_app
Basic Python Django App

#Required DJango Important Command
```
mkdir pythonproject
cd pythonproject
```

#Install virtualend
```
pip install virtualenv
```

#create virtualend and actiavte
```
virtualenv envdev
cd envdev
cd Scripts
activate
cd ..
```

#Install django
```
pip install django
```

#Start django project
```
django-admin startproject MYSITE
python manage.py runserver 5000
```

#Start django project app
```
python manage.py startapp customer
```

#Migrate model
```
python manage.py makemigrations
python manage.py migrate
```

#create super admin user
```
python manage.py createsuperuser
```
#Install PostgreSQL Package in Django
```
pip install django psycopg2
```
#PostgreSQl command for create DB, User and role
#------------------------------
```
CREATE DATABASE agencies;
CREATE USER django WITH PASSWORD 'password';
ALTER ROLE django SET client_encoding TO 'utf8'; 
ALTER ROLE django SET default_transaction_isolation TO 'read committed'; 
ALTER ROLE django SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE agencies TO django;
```

#Setting DB in Django setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sarvesh'
        'USER': 'Password'
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
