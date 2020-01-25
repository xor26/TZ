from bson import ObjectId
from pymongo import MongoClient
from configs import MongoConfig as Conf
from models import User


class MongoGateway:

    def __init__(self):
        client = MongoClient(Conf.HOST, Conf.PORT)
        db = client[Conf.DB_NAME]
        self.collection = db[Conf.COLLECTION]

    def get_user_by_id(self, user_id: ObjectId) -> User:
        return self.collection.find_one({"_id": user_id})

    def get_users(self):
        for user in self.collection.find():
            yield user

    def change_photo(self, user_id: ObjectId, new_photo: str):
        self.collection.update_one({"_id": user_id}, {"$set": {"photo": new_photo}})

    def insert_user(self, user: User):
        result = self.collection.insert_one({"name": user.name, "photo": user.photo})
        if result:
            user_id = result.inserted_id
            return user_id
        else:
            return False

    def purge_db(self):
        self.collection.delete_many({})
