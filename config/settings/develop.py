from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)wma!1ac2r9uy#bp%mzf7nwa%4jjx(@xli6a-j&d@vg0r57@9#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'blog',
    #     'USER': 'nanahiryu',
    #     'PASSWORD': 'ryu2751x7',
    #     'HOST': 'localhost',
    #     'PORT': ''
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
