# My Reddit Clone

Welcome to my Reddit Clone. This is my 4th milestone project for the code institute course. The purpose of this project is to create a full stack web app, making use of a Full Stack Framework, and connecting it to a database to demonstrate CRUD functionality.

My Reddit clone will give the user the ability to create posts and share their ideas and content with each other. Posts can be upvoted and are shown in chronological order.

The project is hosted as a heroku app here: [My Reddit Clone](https://)

## Table of Contents

[Deployment](#deployment)


## Deployment
I deployed my Django app to Heroku early to avoid any issues with deployment and to make testing easier by operating in the environment that the app was going to be hosted in.

1. I created an elephant SQL DB to host my models and data.
![Elephant SQL Dashboard](docs/images/Elephant_sql_dashboard.png)*My Elephant SQL Dashboard*


2. I created the Heroku app that was going to host my project.
![Heroku app Dashboard](docs/images/Heroku_app_dashboard.png)*My Heroku App Dashboard*


3. I connected my GitHub repo housing my project code to my Heroku app using the Heroku GUI.
![Connect GitHub repo to Heroku app](docs/images/Heroku_link_repo.png)*Link Heroku and GitHub repo*


4. I created 3 new config variables in the Heroku app settings for the hosted version of the project to access the external resources it needed, e.g static files on Cloudinary and the Elephant SQL database.<br>
(I created a variable called DISABLE_COLLECTSTATIC with a value of 1 to prevent Heroku from trying to retrieve static files that arent populated yet during early deployment.)
![Heroku Config Variables](docs/images/Heroku_config_vars.png)*My Heroku config Variables*


5. I created an env.py file with a similar set of config variables for use in local development, so that testing could be done on the local server before being pushed to the Heroku platform. This file was in the .gitgnore file as it contained private information for use in development only.
    ```
    import os
    os.environ["DATABASE_URL"] = \
        'my_database_url'

    os.environ["SECRET_KEY"] = \
        'super_secret_key'

    os.environ['CLOUDINARY_URL'] = \
        'my_cloudinary_url'
    ```

6. I updated the installed apps list in the settings.py file to let the django framework know that it was okay to use cloudinary as a place to pull resources from. I also updated the Django constants relating to static file paths and media storage paths in settings.py to also use Cloudinary based assets.
    ```
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = \
        'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/Media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```
    The templates path also needed to be updated here, as well as the templates key telling Django where to look for templates in the default TEMPLATES object.
    ```
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    
    # and
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            .
            .
            .
                ],
            },
        },
    ]
    ```

7. I updated the ALLOWED_HOSTS constant to let Django know that my Heroku App had permission to host its content. I also added localhost to allow the app to be run on a local development server.
    ```
    ALLOWED_HOSTS = ['reddit-clone-matt-m.herokuapp.com', 'localhost']
    ```

8. I created the required directories to store assets in: media, templates and static, as well as creating a Procfile (Process file) to instruct Heroku on how to run the project, and whether it should run the app as a webserver or not. I used [gunicorn](#gunicorn) as the webserver to handle my projects http requests.
    ```
    web: gunicorn reddit_clone.wsgi
    ```

9. The app was ready for deployment and showed the Django skeleton template for an empty Django app when viewing on the Heroku app link.
![First Deployment to Heroku](docs/images/heroku_django_skeleton.png)*Django Skeleton Template hosted on Heroku*