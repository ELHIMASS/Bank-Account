from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from datetime import timedelta
from app.services.user_service import UserService
from app.services.bankAccount_service import BankAccountService
from app.models.user_model import User
from app.Logger.logger import Logger
from flask import current_app


user = Blueprint('user', __name__)
logger = Logger("app.log")



@user.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=10)

@user.route('/')
def index():
    bank= BankAccountService()
    if "username" in session:
        if session["isAdmin"] == True:
            return render_template('index.html')
        else:
            accounts = bank.get_all_accounts_by_user(session["id"])
            return render_template('index.html', accounts=accounts)
            
    return redirect(url_for("user.login"))    

@user.route('/connection', methods=['GET', 'POST'])
def login():
    
    user_service = UserService()
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = user_service.get_by_name(username)
        if user and user.password == password and user.name == username:
            session.permanent = True  
            session["id"] = user.id
            session["username"] = user.name  
            session["isAdmin"] = user.is_admin
            logger.log("info", f"L'utilisateur s'est connecté avec succès {username} .")
            return redirect(url_for("user.index"))
        else:
            logger.log("warning", "Tentative de connexion suspecte détectée.")
            return redirect(url_for("user.login"))

    return render_template("connection.html")


@user.route('/logout')
def logout():
    usr = session["username"]
    logger.log("info", f"déconnection de {usr}.")  
    session.pop("username", None)
    return redirect(url_for("user.index"))

@user.route('/creatUser', methods=['GET', 'POST'])
def creatUser():
    user_service = UserService()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password == confirm_password:
            user_service.create(User(id=0,name=username,password=password,is_admin=False))
            logger.log("info", f"Création de l'utilisateur {username} .")
        return redirect(url_for("user.index"))   


    return render_template("creeUser.html")


