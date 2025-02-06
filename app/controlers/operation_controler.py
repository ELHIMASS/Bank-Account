from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from app.services.bankAccount_service import BankAccountService
from datetime import timedelta
from flask import current_app


operation = Blueprint('operation', __name__)
bankAccount = BankAccountService()



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
        """operationService.create_transfer(Operation(bank_account_id=sender_id,
                                                    type_operation='transfer',
                                                    amount=amount,
                                                    receiver_account_id=receiver_id,
                                                    sender_account_id=sender_id))
        operationService.create_transfer(Operation(bank_account_id=receiver_id,
                                                    type_operation='transfer',
                                                    amount=amount,
                                                    receiver_account_id=receiver_id,
                                                    sender_account_id=sender_id))"""
        
        bankAccount.update_amount(bankAccount.get_by_id(sender_id), -amount)
        bankAccount.update_amount(bankAccount.get_by_id(receiver_id), amount)
        return render_template('index.html')
    
    acounts = bankAccount.get_cheking()
    return render_template('transfer.html', acounts=acounts)




