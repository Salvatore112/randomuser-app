from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from services import UserService

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    users_data = UserService.fetch_users(1000)
    UserService.save_users(users_data)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        count = int(request.form.get("count", 20))
        if count > 0:
            users_data = UserService.fetch_users(count)
            UserService.save_users(users_data)
        return redirect(url_for("index"))

    page = request.args.get("page", 1, type=int)
    pagination = UserService.get_users_paginated(page=page)
    return render_template("index.html", pagination=pagination)


@app.route("/user/<int:user_id>")
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)


@app.route("/random")
def random_user():
    user = UserService.get_random_user()
    if not user:
        return "No users in database", 404
    return render_template("user.html", user=user)


@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        users_data = UserService.fetch_users(1000)
        UserService.save_users(users_data)
    print("Database initialized")


@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        users_data = UserService.fetch_users(1000)
        UserService.save_users(users_data)
    print("Database initialized")


if __name__ == "__main__":
    app.run(debug=True)
