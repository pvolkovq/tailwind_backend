import uuid
from storages.backends.s3boto3 import S3Boto3Storage

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f"{uuid.uuid4().hex}.{ext}"

class MediaStorage(S3Boto3Storage):
    location = "media"          
    file_overwrite = False      
    default_acl = "public-read"
    
class StaticStorage(S3Boto3Storage):
    location = "static"
    file_overwrite = False