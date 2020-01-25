import celery as celery
from PIL import Image
from bson import ObjectId

from configs import CeleryConfig as Conf
from configs import MongoConfig
from mongo_gateway import MongoGateway

data_broker = f"mongodb://{MongoConfig.HOST}:{MongoConfig.PORT}/{MongoConfig.DB_NAME}"
app = celery.Celery("mongodb", broker=data_broker)


@celery.task
def resize_photo(user_id, photo_path):
    img = Image.open(photo_path)
    file_name = img.filename.split("/")[-1]
    new_photo_path = f"{Conf.PROCESSED_IMG_FOLDER}/{file_name}"
    img = img.resize((Conf.IMAGE_WIDTH, Conf.IMAGE_HEIGHT), Image.ANTIALIAS)
    img.save(new_photo_path)
    db_gate = MongoGateway()
    db_gate.change_photo(user_id=ObjectId(user_id), new_photo=new_photo_path)
