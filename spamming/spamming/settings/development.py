import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '0)-6_948xc+g!=!$j^#ad0a)1pf#%ge*41!&om8m2r#r^v@nd2'

DEBUG = True

ALLOWED_HOSTS = []
ROOT_URLCONF = 'spamming.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'