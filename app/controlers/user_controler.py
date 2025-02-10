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
            session["isAdmin"] = user.is_admin
            return redirect(url_for("user.index"))
        else:
            return redirect(url_for("user.login"))

    return render_template("connection.html")


@user.route('/logout')
def logout():
    session.pop("username", None)  # Supprime l'utilisateur de la session
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for("user.index"))



@user.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Vérification de la correspondance des mots de passe
        if password != confirm_password:
            flash("Les mots de passe ne correspondent pas.", "danger")
            return redirect(url_for('user.ajouter'))

        # Simulation de l'ajout de l'utilisateur (remplacez par votre logique de base de données)
        try:
            # Ajoutez votre logique d'ajout à la base ici
            flash(f"Utilisateur '{username}' créé avec succès !", "success")
            return redirect(url_for('index'))  # Redirection vers la page d'accueil
        except Exception as e:
            flash(f"Erreur lors de la création de l'utilisateur : {e}", "danger")
            return redirect(url_for('user.ajouter'))

    return render_template('adduser.html')