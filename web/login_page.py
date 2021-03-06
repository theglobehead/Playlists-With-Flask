import flask
from flask import Blueprint, render_template, request, session, redirect, url_for

from controllers.controller_user import ControllerUser

login_view = Blueprint("login", __name__)


@login_view.route("/", methods=['GET', 'POST'])
def login():
    """
    View for the login page.
    if the method is POST and the form data is valid, it logs the user in
    :return: renders the login view or redirects to the your_playlists view
    """
    result = render_template("login_page.html")

    if request.method == "POST":
        form = request.form
        name = form.get("username").strip()
        password = form.get("password").strip()

        user = ControllerUser.authenticate_user(name, password)
        print("login:", user)

        if user:
            session["user"] = user
            print("set user")
            result = redirect(url_for("playlists.your_playlists"))
        else:
            flask.flash("Incorrect login details!")

    return result
