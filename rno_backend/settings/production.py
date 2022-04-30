from .base import *

DEBUG = False

ALLOWED_HOSTS = ["rno_backend.herokuapp.com",
                 "rno_backend.pythonanywhere.com"]

SESSION_COOKIE_DOMAIN = '.marketbackground.com'

SESSION_COOKIE_SECURE = True
CRSF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000  # one Y
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
