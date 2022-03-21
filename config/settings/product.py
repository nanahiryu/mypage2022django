from .base import *
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['160.251.53.103', 'localhost',
                 'nanahiryu.com', 'www.nanahiryu.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME_SQL'),
        'USER': env('DB_USER_SQL'),
        'PASSWORD': env('DB_PASSWORD_SQL'),
        'HOST': env('DB_HOST_SQL'),
        'PORT': 5432 if DEBUG else '',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
