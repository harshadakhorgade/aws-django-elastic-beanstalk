from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'  # Allow public access for static files

class MediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'private'  # Media files should remain private
    file_overwrite = False
