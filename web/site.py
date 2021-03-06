from flask import Blueprint, session, redirect, url_for

from controllers.controller_song import ControllerSong
from controllers.controller_user import ControllerUser

site = Blueprint("site", __name__)


@site.route("/logout", methods=['GET', 'POST'])
def logout():
    """
    Used for logging a user out.
    Clears the session
    :return: Redirects to the login view
    """
    session["user"] = None
    session.clear()
    return redirect(url_for("login.login"))


@site.route("/profile_picture/<user_uuid>", methods=['GET', 'POST'])
def get_profile_pic(user_uuid: str) -> bytes:
    """
    Used for getting the profile picture of a user
    :param user_uuid: uuid od the song
    :return: returns the image as a response
    """
    result = ControllerUser.get_profile_pic(user_uuid)
    return result


@site.route("/songe_picture/<song_uuid>", methods=['GET', 'POST'])
def get_song_pic(song_uuid: str) -> bytes:
    """
    Used for getting the image for a song
    :param song_uuid: uuid od the song
    :return: returns the image as a response
    """
    result = ControllerSong.get_song_pic(song_uuid)
    return result


