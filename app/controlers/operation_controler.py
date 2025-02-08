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

@operation.route('/retirer', methods=['GET', 'POST'])
def retirer():
    if request.method == 'POST':
        account_id = request.form['id_account']
        amount = float(request.form['amount'])
        
        # Exécuter l'opération de retrait
        op.create_retirer(account_id, amount)

        return render_template('index.html')

    accounts = bankAccount.get_cheking()  # Récupérer les comptes disponibles
    return render_template('retirer.html', accounts=accounts)



@operation.route('/rechercher', methods=['GET', 'POST'])
def rechercher():
    if request.method == 'POST':
        account_id = int(request.args["account_id"]) or None
        account_type = str(request.args["account_type"]) or None
        min_balance = float(request.args["min_balance"]) or None
        max_balance = float(request.args["max_balance"]) or None
        
        accounts = bankAccount.search_accounts(account_id, account_type, min_balance, max_balance)
        return render_template('rechercher.html', accounts=accounts)
    return render_template('rechercher.html', accounts=None)

@operation.route('/account/<int:account_id>/history', methods=['GET'])
def account_history(account_id):
    account = bankAccount.get_by_id(account_id)

    if not account:
        flash("Compte introuvable", "danger")
        return redirect(url_for('operation.rechercher'))  # Correction ici

    # Récupérer toutes les opérations de ce compte
    history = op.get_operations_by_account(account_id)

    return render_template('historique.html', account=account, history=history)




