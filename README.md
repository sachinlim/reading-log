# Personal Reading Log

This is a website made with Django for the backend framework, and a Postgres database to store the data.

### To do list:
- [x] CRUD operations
- [x] Display currently reading books separate from books not fully *started*
- [x] User accounts and authentication
- [ ] Simple UI for use and navigation
- [x] Search bar
- [ ] Pomodoro timer (Javascript)
- [ ] REST APIs with Django REST framework

## Prerequisites

Setting up the project is quite simple, as only Django and Postgres needs to be set up.

```
pip install django psycopg2
```

### Database - Postgres

As the default database of choice is SQLite, the configurations in the [settings.py](reading_log/settings.py) file needs to be changed to accommodate the Postgres database. 

The [configuration](https://github.com/sachinlim/reading-log/blob/3fec208bfd020de1967eb3a3f8e41a7fa78e1050/reading_log/settings.py#L77) for Postgres looks like this:

``` Python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'reading_log',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### PythonAnywhere - SQLite

SQLite was also used when testing out [PythonAnywhere](https://www.pythonanywhere.com/) to host the website online. SQLite allows for quick deployment, as not much needs to be configured for SQLite, and Postgres is only available on their paid plan. The performance was also good enough for this project, as there is not much writing going on, meaning that migrating back to SQLite for quick local deployment would be feasible.

The default connection for SQLite:
``` Python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

