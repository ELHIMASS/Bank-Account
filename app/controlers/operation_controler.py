from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from app.services.bankAccount_service import BankAccountService
from app.services.operation_service import OperationService
from app.models.operation_model import Operation
from datetime import timedelta
from flask import current_app


operation = Blueprint('operation', __name__)
bankAccount = BankAccountService()
op = OperationService()


@operation.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=5)

@operation.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        sender_id = request.form['sender_account']
        receiver_id = request.form['receiver_account']
        amount = float(request.form['amount'])
        # ajoiute un transfer et modifie le montant des deux compte
        op.create_transfer(sender_id, receiver_id, amount)

        return render_template('index.html')
    
    acounts = bankAccount.get_cheking()
    return render_template('transfer.html', acounts=acounts)


@operation.route('/deposer', methods=['GET', 'POST'])
def deposer():
    if request.method == 'POST':
        account_id = request.form['id_account']
        amount = request.form['amount']

        op.create_deposit(account_id, amount)
        return render_template('index.html')
    
    acounts = bankAccount.get_all()
    return render_template('deposer.html', acounts=acounts)


