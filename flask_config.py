import os


class FlaskConfig(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "xxx"
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or "file_storage/images_original"

