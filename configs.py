import os


class FlaskConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "xxx"
    UPLOAD_FOLDER = "file_storage/images_original"


class MongoConfig:
    HOST = "localhost"
    PORT = 27017
    DB_NAME = "examples"
    COLLECTION = "inventory"

