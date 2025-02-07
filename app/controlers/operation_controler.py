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
    accounts = bankAccount.get_all()  # Récupérer tous les comptes par défaut

    if request.method == 'POST':
        search_input = request.form.get('search_input')

        # Vérifier si l'entrée est un ID (numérique)
        if search_input.isdigit():
            accounts = bankAccount.search_accounts(account_id=int(search_input))

        # Vérifier si c'est un type de compte
        elif search_input.lower() in ["checking", "saving"]:
            accounts = bankAccount.search_accounts(account_type=search_input.lower())

        # Vérifier si c'est un solde (nombre avec décimale possible)
        else:
            try:
                balance = float(search_input)
                accounts = bankAccount.search_accounts(min_balance=balance, max_balance=balance)
            except ValueError:
                flash("Veuillez entrer un ID, un type de compte ou un solde valide.", "danger")

    return render_template('rechercher.html', accounts=accounts)

@operation.route('/account/<int:account_id>/history', methods=['GET'])
def account_history(account_id):
    account = bankAccount.get_by_id(account_id)

    if not account:
        flash("Compte introuvable", "danger")
        return redirect(url_for('operation.rechercher'))  # Correction ici

    # Récupérer toutes les opérations de ce compte
    history = op.get_operations_by_account(account_id)

    return render_template('historique.html', account=account, history=history)




