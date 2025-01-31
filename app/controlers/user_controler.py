from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from datetime import timedelta
from app.services.user_service import UserService
from app.models.user_model import User

from flask import current_app


user = Blueprint('user', __name__)
user_service = UserService()


@user.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=5)

@user.route('/')
def index():
    return render_template('index.html')

@user.route('/connection', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = user_service.get_by_name(username)
        if user :
            session.permanent = True  # Active la session persistante
            session["username"] = user.name  # Stocke le nom d'utilisateur dans la session
            flash("Connexion réussie !", "success")
            return redirect(url_for("user.index"))
        else:
            return redirect(url_for("user.login"))

    return render_template("connection.html")


@user.route('/logout')
def logout():
    session.pop("username", None)  # Supprime l'utilisateur de la session
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for("user.index"))
