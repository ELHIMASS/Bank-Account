from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from app.services.bankAccount_service import BankAccountService
from datetime import timedelta
from flask import current_app


operation = Blueprint('operation', __name__)



@operation.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=5)

@operation.route('/transfer', methods=['GET', 'POST'])
def transfer():
    #acounts = bankAccount.get_cheking()
    return render_template('transfer.html')




