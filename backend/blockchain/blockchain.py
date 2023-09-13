from backend.blockchain.block import Block

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


def main():
    blockchain= Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain.json_type())
if __name__=='__main__':
    main()