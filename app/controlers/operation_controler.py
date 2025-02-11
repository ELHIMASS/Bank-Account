from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from app.services.bankAccount_service import BankAccountService
from app.services.operation_service import OperationService
from app.models.operation_model import Operation
from datetime import timedelta
from flask import current_app


operation = Blueprint('operation', __name__)



@operation.before_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=5)

@operation.route('/transfer', methods=['GET', 'POST'])
def transfer():
    bankAccount = BankAccountService()
    op = OperationService()
    if session["isAdmin"] == True:
        
        if request.method == 'POST':
            sender_id = request.form['sender_account']
            receiver_id = request.form['receiver_account']
            amount = float(request.form['amount'])
            # ajoiute un transfer et modifie le montant des deux compte
            op.create_transfer(sender_id, receiver_id, amount)

            return redirect(url_for("user.index"))
        
        acounts = bankAccount.get_cheking()
        return render_template('transfer.html', acounts=acounts)
    else:
        if request.method == 'POST':
            sender_id = request.form['sender_account']
            receiver_id = request.form['receiver_account']
            amount = float(request.form['amount'])
            # ajoiute un transfer et modifie le montant des deux compte
            op.create_transfer(sender_id, receiver_id, amount)

            return redirect(url_for("user.index"))
        
        acounts = bankAccount.get_all_accounts_by_user(session["id"])
        return render_template('transfer.html', acounts=acounts)
        


@operation.route('/deposer', methods=['GET', 'POST'])
def deposer():
    bankAccount = BankAccountService()
    op = OperationService()
    if request.method == 'POST':
        account_id = request.form['id_account']
        amount = request.form['amount']

        op.create_deposit(account_id, amount)
        return render_template('index.html')
    
    acounts = bankAccount.get_all()
    return render_template('deposer.html', acounts=acounts)

@operation.route('/retirer', methods=['GET', 'POST'])
def retirer():
    bankAccount = BankAccountService()
    op = OperationService()
    if request.method == 'POST':
        account_id = request.form['id_account']
        amount = float(request.form['amount'])
        
        # Exécuter l'opération de retrait
        op.create_retirer(account_id, amount)

        return render_template('index.html')

    accounts = bankAccount.get_cheking()  # Récupérer les comptes disponibles
    return render_template('retirer.html', accounts=accounts)



@operation.route('/rechercher', methods=['GET'])
def rechercher():
    bankAccount = BankAccountService()

    account_id = request.args.get('account_id', None)
    account_type = request.args.get('account_type', None)
    min_balance = request.args.get('min_balance', None)
    max_balance = request.args.get('max_balance', None)

    # Convertir les valeurs
    account_id = int(account_id) if account_id else None
    min_balance = float(min_balance) if min_balance else None
    max_balance = float(max_balance) if max_balance else None

    # Recherche des comptes
    accounts = bankAccount.search_accounts(account_id, account_type, min_balance, max_balance)
    return render_template('rechercher.html', accounts=accounts)




@operation.route('/account/<int:account_id>/history', methods=['GET'])
def account_history(account_id):
    bankAccount = BankAccountService()
    op = OperationService()
    
    account = bankAccount.get_by_id(account_id)

    if not account:
        flash("Compte introuvable", "danger")
        return redirect(url_for('operation.rechercher'))

    history = op.get_operations_by_account(account_id)

    return render_template('historique.html', account=account, history=history)




