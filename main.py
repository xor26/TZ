import os
import time

from bson import ObjectId
from flask import Flask, render_template, request, redirect
from configs import FlaskConfig
from forms import UserAddForm
from models import User
from mongo_gateway import MongoGateway
from tasks import resize_photo as resize_photo_celery_task
from bson.json_util import dumps

app = Flask(__name__)
app.config.from_object(FlaskConfig)
mongo = MongoGateway()


@app.route("/", methods=["GET"])
def user_list():
    return render_template("user_list.html", title="Users", users=mongo.get_user_list())


@app.route("/add", methods=["GET"])
def user_add_form_request():
    form = UserAddForm()
    return render_template("user_add.html", title="Add new user", form=form)


@app.route("/add", methods=["POST"])
def user_add_form_send():
    # TODO add data validation here

    photo = request.files["photo"]
    file_format = photo.filename.split('.')[-1]
    new_file_name = str(time.time()).replace(".", "")
    new_file_name = f"{new_file_name}.{file_format}"
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)
    photo.save(photo_path)

    user = User(name=request.form.get("name"), photo=photo_path)
    user_id = mongo.insert_user(user=user)

    resize_photo_celery_task.delay(user_id=str(user_id), photo_path=photo_path)

    return redirect("/")


@app.route("/api/users", methods=["GET"])
def api_get_user_list():
    users = list(mongo.get_user_list())
    response = app.response_class(
        response=dumps(users),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/users/<user_id>", methods=["GET"])
def api_get_user_by_id(user_id):
    user_id = ObjectId(user_id)
    user = mongo.get_user_by_id(user_id)
    response = app.response_class(
        response=dumps(user),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run()
