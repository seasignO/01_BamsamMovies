from .base import * # base에서 전체 상속
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='il&y7d^ipflr$@r-_ymd*ib9nt@k289erb_5xkdz&%cc5i%_$2')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []