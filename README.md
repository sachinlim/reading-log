# Personal Reading Log

This is a website made with Django for the backend framework, and a Postgres database to store the data. The main purpose was to learn about Django and its viability of using its templates to deploy websites. [PythonAnywhere](https://www.pythonanywhere.com/) was also used to test this website being hosted online without `localhost` being used. 

Compared to the previous [web application](https://github.com/sachinlim/after-school-activity-website) that I made, using Django was a bit easier because there's no more SQL statements to worry about due to the ORM. Learning about the Django REST framework also showed the possibilities of RESTful APIs in the same way as with Spring Boot, and opens up the door to separate Django for the backend and having a separate frontend framework like React or Angular. 


## Features 

* Users can sign up for the website and track their own books
* Users can add new books that they are currently reading or planning on reading 
  - Home page will separate the two lists of current and planned books
* Users can edit book details to keep track of progress
* Users can delete books from their Log
* Users can write a summary about the books, like a review, and write about what they have learnt from the book
* Users can tick a box to show if they'd recommend the book or not



### Project Plan:
- [x] CRUD operations
- [x] Display currently reading books separate from books not fully *started*
- [x] User accounts and authentication
- [x] Allow users to update their password
- [x] Simple UI for use and navigation
- [x] Search bar
- [x] Test out REST APIs with Django REST framework
- [ ] Pomodoro timer (Javascript)

## Prerequisites

Setting up the project is quite simple, as only Django and Postgres needs to be set up, with the Django REST framework being an extra for the use of RESTful APIs. 

```
pip install django psycopg2 djangorestframework 
```

The Django REST framework was added later on to handle API requests, and [Postman](https://www.postman.com/) was used to make the requests. PyCharm Professional does have a [HTTP client](https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html), but it was not used in favour of Postman for this project.

### Database - Postgres

As the default database of choice is SQLite, the configurations in the [settings.py](reading_log/settings.py) file needs to be changed to accommodate the Postgres database. The [configuration](https://github.com/sachinlim/reading-log/blob/3fec208bfd020de1967eb3a3f8e41a7fa78e1050/reading_log/settings.py#L77) for Postgres looks like this:

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

### PythonAnywhere - SQLite

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

## Screenshots

## Future Plans

Now that the skeleton for the website has been made, it could be used to make a full-fledged website where people can interact with the other users. For example, some of the possibilities:

* Make the website fully utilise REST APIs and have a separate frontend framework
* See reviews about books made by other users
* See a list of books that are highly recommended
* See what people are reading or planning on reading
* A forum page where people can ask about new books to read or share what people have learnt

Although this project does need to factor in external issues such as GDPR because data is being stored about users, it would be even more crucial when implementing the features described above. 

