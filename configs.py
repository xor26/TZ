import os


class FlaskConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "xxx"
    UPLOAD_FOLDER = "file_storage/images_original"
    USERS_PER_PAGE = 3


class MongoConfig:
    HOST = "localhost"
    PORT = 27017
    DB_NAME = "test"
    COLLECTION = "inventory"


class CeleryConfig:
    IMAGE_WIDTH = 150
    IMAGE_HEIGHT = 150
    PROCESSED_IMG_FOLDER = "file_storage/images_processed"
