from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
