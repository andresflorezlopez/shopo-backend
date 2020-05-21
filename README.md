## shopo backend

Everyone has to clone the repository and execute the following commands:

# Install dependencies:
```
pipenv install
```

# Activate the virtual env
```
pipenv shell
```

# Create tables in database
```
pyhton manage.py migrate
```

# Run application
```
pyhton manage.py runserver
```
# Create new app inside the project
```
django-admin startapp products
```

# Folder structer
```
├── Pipfile
├── Pipfile.lock
├── README.md
├── categories
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── shopobackend
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```