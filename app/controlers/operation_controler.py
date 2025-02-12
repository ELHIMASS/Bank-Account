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
    current_app.permanent_session_lifetime = timedelta(minutes=10)

#done ?? log
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
        

#done ?? log
@operation.route('/deposer', methods=['GET', 'POST'])
def deposer():
    if session["isAdmin"] == True:
        bankAccount = BankAccountService()
        op = OperationService()
        if request.method == 'POST':
            account_id = request.form['id_account']
            amount = request.form['amount']

            op.create_deposit(account_id, amount)
            return redirect(url_for("user.index"))
        
        acounts = bankAccount.get_all()
        return render_template('deposer.html', acounts=acounts)
    else:
        return "tu n'est pas admin "


#done ?? log
@operation.route('/retirer', methods=['GET', 'POST'])
def retirer():
    bankAccount = BankAccountService()
    op = OperationService()
    if session["isAdmin"] == True:
        if request.method == 'POST':
            account_id = request.form['id_account']
            amount = float(request.form['amount'])
            
            # Exécuter l'opération de retrait
            op.create_retirer(account_id, amount)

            return redirect(url_for("user.index"))

        accounts = bankAccount.get_cheking()  # Récupérer les comptes disponibles
        return render_template('retirer.html', accounts=accounts)
    else:
        if request.method == 'POST':
            account_id = request.form['id_account']
            amount = float(request.form['amount'])
            
            op.create_retirer(account_id, amount)

            return redirect(url_for("user.index"))
        # recupere les compte lier au user
        accounts = bankAccount.get_all_accounts_by_user(session["id"]) 
        return render_template('retirer.html', accounts=accounts) 

#done ?? log
@operation.route('/rechercher', methods=['GET'])
def rechercher():
    if session["isAdmin"] == True:
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
    else:
        return "tu n'est pas un admin"



#done ?? log
@operation.route('/account/<int:account_id>/history', methods=['GET'])
def account_history(account_id):
    if session["isAdmin"] == True:
        bankAccount = BankAccountService()
        op = OperationService()
        
        account = bankAccount.get_by_id(account_id)

        if not account:
            flash("Compte introuvable", "danger")
            return redirect(url_for('operation.rechercher'))

        history = op.get_operations_by_account(account_id)

        return render_template('historique.html', account=account, history=history)
    else:
        return "tu n'est pas un admin"
    
    
    
    

@operation.route('/history', methods=['GET'])
def user_history():
    if "id" not in session:
        flash("Veuillez vous connecter pour voir l'historique.", "danger")
        return redirect(url_for("user.login"))

    user_id = session["id"]  # ID de l'utilisateur connecté
    operation_service = OperationService()
    bank_account_service = BankAccountService()

    # Récupérer tous les comptes de l'utilisateur
    accounts = bank_account_service.get_all_accounts_by_user(user_id)

    if not accounts:
        flash("Aucun compte trouvé pour cet utilisateur.", "info")
        return redirect(url_for("user.index"))

    # Récupérer les historiques de chaque compte
    history = {}
    for account in accounts:
        history[account.id] = operation_service.get_operations_by_account(account.id)

    return render_template("user_history.html", accounts=accounts, history=history)


