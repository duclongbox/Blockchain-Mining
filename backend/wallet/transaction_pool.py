class TransactionPool:
    def __init__(self):
        self.transactionMap = {}
    def set_transaction(self,transaction):
        """
        set a transaction in a transaction pool
        """
        self.transactionMap[transaction.id] = transaction
