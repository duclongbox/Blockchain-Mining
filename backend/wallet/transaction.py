import time
import uuid
from backend.wallet.wallet import Wallet


class Transaction:
    """
    Document of an exchange in currency from sender to recipients
    """
    def __init__(self, wallet_sender, recipient,amount):
        self.id = str(uuid.uuid4())[:8]
        self.output = self.create_output(wallet_sender, recipient,amount)
        self.input = {
            'timestamp' :time.time_ns(),
            'amount': wallet_sender.balance,
            'address': wallet_sender.address,
            'public_key': wallet_sender.public_key,
            'signature' : wallet_sender.sign(self.output)
        }
    
    def create_output(self,wallet_sender,recipient, amount):
        """
        structure ouput for the transaction
        """
        if amount> wallet_sender.balance:
            raise Exception('Amount exceeded')
        output = {}
        output[recipient] = amount # asign the amount to recipient
        output[wallet_sender.address] = wallet_sender.balance - amount  #asign balance of sender
        
        return output
    
    def update_transaction(self,wallet_sender,recipient, amount):
        """
        update the transaction with an existing or new recipient.
        """
        if amount > self.output[wallet_sender.address]:
            raise Exception('Amount exceeding balance')
        
        if recipient in self.output:
            self.output[recipient] += amount
        else:
            self.output[recipient] = amount
        self.output[wallet_sender.address]-= amount
        self.input  = {
            'timestamp' :time.time_ns(),
            'amount': wallet_sender.balance,
            'address': wallet_sender.address,
            'public_key': wallet_sender.public_key,
            'signature' : wallet_sender.sign(self.output)
        }
    def json_type(self):
        """
        serialize the transaction
        """
        return self.__dict__
    @staticmethod
    def is_validate_trans(transaction):
        total_output = sum(transaction.output.values())
        if(transaction.input['amount']) != total_output:
            raise Exception('invalid output transaction')
        if not  Wallet.verify(transaction.input['public_key'],transaction.output,transaction.input['signature']):
            raise Exception('invalid signature')
   
def main():
    transaction = Transaction(Wallet(),'receive',39)
    print(transaction.__dict__)
if __name__ == '__main__':
    main()
        