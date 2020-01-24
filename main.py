import os

from flask import Flask, render_template, request, redirect
from configs import FlaskConfig
from forms import UserAddForm
from models import User
from mongo_gateway import MongoGateway
from tasks import resize_photo as resize_photo_celery_task

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
    # TODO add validation here

    photo = request.files["photo"]
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
    photo.save(photo_path)
    # TODO save user to mongo
    user = User(name=request.form.get("name"), photo=photo_path)
    user_id = mongo.insert_user(user=user)

    # TODO run celery resize task
    resize_photo_celery_task.delay(user_id=user_id, photo_path=photo_path)
    return redirect("/")


if __name__ == "__main__":
    app.run()
