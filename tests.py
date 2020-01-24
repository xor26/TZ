import unittest

from models import User
from mongo_gateway import MongoGateway
from tasks import resize_photo


class TestApp(unittest.TestCase):
    def setUp(self):
        # TODO create db for test and mock it in DB_NAME in MongoConfig class
        self.mongo = MongoGateway()
        self.mongo.purge_db()

    def test_insert_user(self):
        user = User(name="Test User", photo="test_photo.jpg")
        user_id = self.mongo.insert_user(user=user)

        self.assertNotEqual(user_id, False)

    def test_resize_img(self):
        user = User(name="Test User Resize", photo="file_storage/images_original/test_photo.jpg")
        user_id = self.mongo.insert_user(user=user)
        resize_photo(user_id=user_id, photo_path=user.photo)

        user = self.mongo.get_user_by_id(user_id)

        self.assertTrue("images_processed" in user["photo"])


if __name__ == '__main__':
    unittest.main()
