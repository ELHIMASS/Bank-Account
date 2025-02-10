from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from datetime import timedelta
from app.services.user_service import UserService
from app.services.bankAccount_service import BankAccountService
from app.models.user_model import User

from flask import current_app


user = Blueprint('user', __name__)
user_service = UserService()
bank= BankAccountService()


@user.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=5)

@user.route('/')
def index():
    if "username" in session:
        if session["isAdmin"] == True:
            return render_template('index.html')
        else:
            accounts = bank.get_all_accounts_by_user(session["id"])
            return render_template('index.html', accounts=accounts)
            
    return redirect(url_for("user.login"))    

@user.route('/connection', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = user_service.get_by_name(username)
        if user :
            session.permanent = True  
            session["id"] = user.id
            session["username"] = user.name  
            session["isAdmin"] = user.is_admin
            return redirect(url_for("user.index"))
        else:
            return redirect(url_for("user.login"))

    return render_template("connection.html")


@user.route('/logout')
def logout():
    session.pop("username", None)  
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for("user.index"))

@user.route('/creatUser', methods=['GET', 'POST'])
def creatUser():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password == confirm_password:
            user_service.create(User(id=0,name=username,password=password,is_admin=False))
        return redirect(url_for("user.index"))   


    return render_template("creeUser.html")


@user.route('/ajouter1', methods=['GET', 'POST'])
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
            return redirect(url_for('index.html'))

    return render_template('adduser.html')