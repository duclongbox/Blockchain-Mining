from backend.wallet.transaction import Transaction
from backend.blockchain.blockchain import Blockchain
class TransactionPool:
    def __init__(self):
        self.transactionMap = {}
    def set_transaction(self,transaction):
        """
        set a transaction in a transaction pool
        """
        self.transactionMap[transaction.id] = transaction
    def existed_transaction(self,address):
        """
        find the existing transaction 
        """
        for transaction in self.transactionMap.values():
            if transaction.input['address'] == address:
                return transaction
    def transaction_query(self):
        """
        allow to query transaction attribute
        """
        transaction_data = list(map(lambda transaction: transaction.json_type(), self.transactionMap.values()))
        return transaction_data
    
    def clear_transaction(self,blockchain):
        """
        Delete blockchain recorded transaction from transaction pool
        """
        for block in blockchain.chain:
            for transaction in block.data:
                try:
                  del self.transactionMap[transaction['id']]
                except Exception:
                    pass