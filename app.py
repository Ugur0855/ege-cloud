from time import sleep
from flask import Flask, stream_with_context, request, Response, flash, render_template, redirect, url_for
from flask_login import LoginManager
from user import get_user
import views

from database import Database

def create_app():
    app = Flask(__name__)
    app.secret_key = '!$w4wW~o|~8OVFX'  # !!change this with random key!!
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.login)
    app.add_url_rule("/logout", view_func=views.logout)
    app.add_url_rule("/index", view_func=views.index)
    app.add_url_rule("/list", view_func=views.list_exams)
    app.add_url_rule("/create_exam", view_func=views.create_exam)

    return app

lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)


if __name__ == '__main__':
    app = create_app()
    port = app.config.get("PORT", 6000)
    app.run(host="127.0.0.1", port=port)
