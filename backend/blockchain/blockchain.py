from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.wallet.wallet  import Wallet
from backend.config import MINING_REWARD_INPUT
class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain=[Block.genesis()]
    def add_block(self,data):
        self.chain.append(Block.mine_block(self.chain[-1],data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'
    
    def replace_chain(self,chain):
        """
        Replace the local chain with the new comming chain:
        -the incomming chain must be longer than local
        -the incomming chain must be valid
        """
        if len(chain)<=len(self.chain):
            raise Exception('the replacement must be longer')
        try: 
            Blockchain.validate_chain(chain)
        except Exception as e:
            print(f'ERROR : {e}')
        self.chain = chain
    
    def json_type(self):
        """
        add block which convert to dict to chain
        """
        block_list = []
        for i in range(len(self.chain)):
            block_list.append(self.chain[i].json_type())
        return block_list
    @staticmethod
    def deserialize(JSON_chain):
        """
        Deserialize of the list of serialized blocks to Blockchain instance
        """
        blockchain = Blockchain()
        block_list =[]
        
        for i in range(len(JSON_chain)):
            block_list.append(Block.deserialize(JSON_chain[i]))
        blockchain.chain = block_list
        return blockchain
        
    @staticmethod
    def validate_chain(chain):
        """
        Validate the incomming chain must follow:
        -the chain must start with the genesis block
        -all the blocks must be valid
        """
        if chain[0].__dict__ != Block.genesis().__dict__:
            raise Exception('the genesis must be valid')
        for i in range(1,len(chain)):
            block = chain[i]
            Block.validate_block(chain[i-1],block)
        Blockchain.validate_transaction_chain(chain)
    @staticmethod
    def validate_transaction_chain(chain):
        """
        Enforce the rule of chain composed of blocks of transaction:
        -> Each transaction must appreared onnce in chain
        -> one mining reward/block
        -> valid transaction
        """
        transaction_id = set()
        for i in range(len(chain)):
            block = chain[i] 
            is_reward = False
            for transaction_json in block.data:
                transaction = Transaction.deserialize(transaction_json)
                if transaction.id in transaction_id:
                    raise Exception(f'{transaction.id} is not unique')
                if transaction.input == MINING_REWARD_INPUT:
                    if is_reward == True:
                        raise Exception(f'Rewarding should be granted once check {block.hash}')
                    is_reward = True
                else:
                    transaction_id.add(transaction.id)
                    historic_chain = Blockchain()
                    historic_chain.chain = chain[:i]
                    historic_balance = Wallet.calculate_balance(historic_chain,transaction.input['address'])
                    if historic_balance != transaction.input['amount']:
                        raise Exception(f'{transaction.id} has invalid input amount')
                Transaction.is_validate_trans(transaction)

def main():
    blockchain= Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain.json_type())
if __name__=='__main__':
    main()