import os

from flask import Flask, render_template, request, redirect
from flask_config import FlaskConfig
from forms import UserAddForm

app = Flask(__name__)
app.config.from_object(FlaskConfig)


@app.route("/", methods=["GET"])
def user_list():
    users = ["user1", "user2", "user3"]
    return render_template("user_list.html", title="Users", len=len(users), users=users)


@app.route("/add", methods=["GET"])
def user_add_form_request():
    form = UserAddForm()
    return render_template("user_add.html", title="Add new user", form=form)


@app.route("/add", methods=["POST"])
def user_add_form_send():
    photo = request.files['photo']
    if photo:
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))
        return redirect("/")


if __name__ == "__main__":
    app.run()
