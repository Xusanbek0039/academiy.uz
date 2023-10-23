from .base import *



DEBUG = True
SSL_ISSANDBOX = True
ALLOWED_HOSTS = ['*']
DJANGO_ADMIN_URL = 'admin-panel/'
STORE_ID = 'put_your_sslcommerz_store_id_here'
STORE_PASS = 'put_your_sslcommerz_store_password_here'

EMAIL_HOST_USER = 'your_email@example.com'


THIRD_PARTY_APPS += [
    'debug_toolbar',
]
INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


