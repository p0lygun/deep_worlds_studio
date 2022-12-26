import os
from .base import *

DEBUG = False

SECRET_KEY = os.getenv('PRODUCTION_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['stilllearning.tech', '0.0.0.0']

try:
    from .local import *
except ImportError:
    pass
