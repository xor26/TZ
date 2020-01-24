from flask import Flask, render_template
from flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["GET"])
def user_list():
    users = ["user1", "user2", "user3"]
    return render_template("user_list.html", title="Users", len=len(users), users=users)


@app.route("/add", methods=["GET", "POST"])
def user_add():
    return render_template("user_add.html", title="Users")


if __name__ == "__main__":
    app.run()
