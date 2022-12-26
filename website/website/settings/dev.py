from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y67ov*m0363@y=(8-p*jyn)!nb*g*m=rm7a^lnwzg@ria4*8n9"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


try:
    from .local import *
except ImportError:
    pass
