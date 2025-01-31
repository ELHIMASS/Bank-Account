from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session, abort
from datetime import timedelta
from app.services.bankAccount_service import BankAccountService
from app.models.bankAcount_model import BankAccount

from flask import current_app


bankAccount = Blueprint('bankAccount', __name__)
bank_service = BankAccountService()


@bankAccount.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=5)

@bankAccount.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if session.get("username") == "admin":
        if request.method == "POST":
            balance = request.form.get("balance")
            type_compte = request.form.get("type_compte")
            intereste_rate = request.form.get("interest_rate", None)
            tmp = BankAccount(balance=balance, type_compte=type_compte, interest_rate=intereste_rate)
            bank_service.create(tmp)
            return render_template('index.html')

        return render_template('Acompt.html')
    else:
        abort(404)

@bankAccount.route('/suprimer', methods=['GET', 'POST'])
def supprimer():
    return render_template("connection.html")



