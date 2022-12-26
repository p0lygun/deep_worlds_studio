import os
import json
from .base import *

DEBUG = False

SECRET_KEY = os.getenv('PRODUCTION_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = json.loads(os.getenv('ALLOWED_HOSTS'))
CSRF_TRUSTED_ORIGINS = json.loads(os.getenv('CSRF_TRUSTED_ORIGINS'))

try:
    from .local import *
except ImportError:
    pass
