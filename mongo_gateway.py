from pymongo import MongoClient
from configs import MongoConfig as Conf
from models import User


class MongoGateway:

    def __init__(self):
        client = MongoClient(Conf.HOST, Conf.PORT)
        db = client[Conf.DB_NAME]
        self.collection = db[Conf.COLLECTION]

    def get_user_by_id(self, user_id):
        pass

    def get_user_list(self):
        for user in self.collection.find():
            yield user

    def change_photo(self, user_id, new_photo):
        pass

    def insert_user(self, user: User):
        self.collection.insert_one({"name": user.name, "photo": user.photo})

    def purge_db(self):
        """"delete after"""
        self.collection.delete_many({})
