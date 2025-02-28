from .base import *
import os
from decouple import config  # Ensure `python-decouple` is installed

DEBUG = False

# Set ALLOWED_HOSTS dynamically or use default
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "testing2.us-west-1.elasticbeanstalk.com").split(",")

# Database Configuration - Uses RDS if available, otherwise falls back to SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.getenv('RDS_DB_NAME', 'default_db_name'),
#         'USER': os.getenv('RDS_USERNAME', 'default_user'),
#         'PASSWORD': os.getenv('RDS_PASSWORD', 'default_password'),
#         'HOST': os.getenv('RDS_HOSTNAME', 'default_host'),
#         'PORT': os.getenv('RDS_PORT', '5432'),
#     }
# }

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# AWS S3 Storage Configuration
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

# Static Files (CSS, JS, Images)
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'awsdjango.storage_backends.StaticStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media Files (User Uploads)
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'awsdjango.storage_backends.MediaStorage'
