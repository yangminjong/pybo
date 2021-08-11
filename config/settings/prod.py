from .base import *

ALLOWED_HOSTS = ['3.36.224.185']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '9=zj0PK(vZS]5.aioWLLh8IjttV8>=}1',
        'HOST': 'ls-3544ff5f9c22caae78fe291bc543db1195b9d9e8.cdwtw4ynmmhs.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}