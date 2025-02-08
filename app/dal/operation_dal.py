from app.models.operation_model import Operation
from app.models.bankAcount_model import BankAccount
from app.models.dataBase import sessionLocal

class OperationDAL:
    def __init__(self):
        self.session = sessionLocal()

    def get_all(self):
        return self.session.query(Operation).all()

    def get_by_id(self, id):
        return self.session.query(Operation).get(id)
    
    def create_transfer(self, sender_id, receiver_id, amount):
        sender = self.session.query(BankAccount).filter(BankAccount.id == sender_id).first()
        receiver = self.session.query(BankAccount).filter(BankAccount.id == receiver_id).first()

        if not sender or not receiver:
            raise ValueError("L'un des comptes n'existe pas")

        if sender.balance < amount:
            raise ValueError("Fonds insuffisants")

        transfer = Operation(
            type="transfer",
            amount=amount,
            sender_account_id=sender_id,
            receiver_account_id=receiver_id
        )

        sender.balance -= amount
        receiver.balance += amount

        self.session.add(transfer)
        self.session.commit()
        self.session.refresh(sender)
        self.session.refresh(receiver)
        self.session.refresh(transfer)

        #print(f"🔄 Transfert effectué : {amount} MAD de {sender.id} vers {receiver.id}")
        #print(f"💰 Nouveau solde émetteur : {sender.balance} | bénéficiaire : {receiver.balance}")

    def create_deposit(self, account_id, amount):
        # Récupérer le compte bancaire
        account = self.session.query(BankAccount).filter(BankAccount.id == account_id).first()

        # Créer une opération de dépôt
        deposit = Operation(
            type="deposit",
            amount=amount,
            bank_account_id=account_id
        )

        # Ajouter le montant au solde du compte
        account.balance += float(amount) # type: ignore

        self.session.add(deposit)
        self.session.commit()
        
        self.session.refresh(account)
        self.session.refresh(deposit)
        
        #print(f"💰 Dépôt effectué : {amount} MAD sur le compte {account.id}")
        #print(f"💰 Nouveau solde : {account.balance}") # type: ignore

    def create_retirer(self, account_id, amount):
        account = self.session.query(BankAccount).filter(BankAccount.id == account_id).first()

        if not account:
            raise ValueError("Le compte n'existe pas")

        if account.balance < amount:
            raise ValueError("Fonds insuffisants")

    # Enregistrer l'opération de retrait
        retireral = Operation(
            type="retirer",
            amount=amount, 
            bank_account_id=account_id
    )

        account.balance -= amount  # Débiter le compte

        self.session.add(retireral)
        self.session.commit()
        
        self.session.refresh(account)
        self.session.refresh(retireral)
        
        
        
    
    def search(self, account_id=None, account_type=None, min_balance=None, max_balance=None):
       
        query = self.session.query(BankAccount)

        if account_id:
            query = query.filter(BankAccount.id == account_id)

        if account_type and account_type != "all":
            query = query.filter(BankAccount.type_compte == account_type)

        if min_balance:
            query = query.filter(BankAccount.balance >= float(min_balance))

        if max_balance:
            query = query.filter(BankAccount.balance <= float(max_balance))

        return query.all()
    
    def get_operations_by_account(self, account_id):

        return self.session.query(Operation).filter(
            (Operation.bank_account_id == account_id) |
            (Operation.sender_account_id == account_id) |
            (Operation.receiver_account_id == account_id)
        ).order_by(Operation.id.desc()).all()


    
    def create(self, operation):
        self.session.add(operation)
        self.session.commit()

    def update(self, operation):
        self.session.commit()

    def delete(self, operation):
        self.session.delete(operation)
        self.session.commit()
