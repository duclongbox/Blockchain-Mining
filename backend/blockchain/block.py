import time
from backend.utils.hash import crypto_hash
from backend.utils.conver_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_BLOCK={
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash' : 'genesis_hash',
    'data' : [],
    'difficulty' : 4,
    'nonce' : 'nonce_value'
}
class Block:
    def __init__(self,timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp=timestamp
        self.last_hash=last_hash
        self.hash= hash
        self.data=data
        self.difficulty = difficulty
        self.nonce = nonce
    def __repr__(self):
        return (
            'block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, ' 
            f'hash: {self.hash}, '           
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce}, '
        )
    @staticmethod
    def mine_block(last_block, data):
        """
        mine a block based on the given last_block and data. Until the a block hash is found 
        that meets the leading 0's proof of work requirement. 
        Add adjust_difficulty  
        """
        timestamp=time.time_ns()
        last_hash=last_block.hash
        difficulty = Block.adjust_difficulty(last_block,timestamp)
        nonce = 0   #keep track the number of loop
        hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)
        # create a hash until the leading 0 = difficulty
        while hex_to_binary(hash)[0:difficulty] != '0'* difficulty: #using binary for more precisely
            nonce +=1
            timestamp=time.time_ns()
            difficulty = Block.adjust_difficulty(last_block,timestamp)
            hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce) 

        return Block(timestamp, last_hash, hash,data,difficulty,nonce)
    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        # return Block(1, 'genesis_last_hash', 'genesis_hash',[])
        return Block(**GENESIS_BLOCK) # ** dictionary unpacking take all the value pass as arguments
    @staticmethod
    def adjust_difficulty(last_block,new_timestamp):
        """
        Calculate the adjusted the difficulty according to the MINE_RATE.
        Increase the difficulty if mining is quick
        Decrease the difficulty if mining is slow
        Make sure the difficulty is more than 0
        """
        if (new_timestamp-last_block.timestamp) < MINE_RATE:
            return last_block.difficulty +1 
        if (last_block.difficulty -1 ) > 0:
            return last_block.difficulty -1
        return 1 
    @staticmethod
    def validate_block(last_block,block):
        """
        Validate the block must follow these rules:
        -the block must have proper last_hash reference
        -meet the requirement of PoW
        -the difficulty adjust by 1 avoid hurting the system 
        -the block hash must be a valid combination of the block fields
        """
        if last_block.hash != block.last_hash:
            raise Exception('The last_hash reference must be true')
        if hex_to_binary(block.hash)[0:block.difficulty] != '0'*block.difficulty:
            raise Exception('The block must meet the PoW requirement')
        if abs(block.difficulty-last_block.difficulty) > 1:
            raise Exception('The difficulty must changed by 1 only')
        regenerated_hash= crypto_hash(block.timestamp, block.last_hash, block.data, block.nonce, block.difficulty)
        if regenerated_hash!= block.hash:
            raise Exception('the block hash must be a valid combination of the block fields')

def main():
    genesis_block=Block.genesis()
    bad_block=Block.mine_block(genesis_block,'foo')
    # bad_block.last_hash = 'damk'
    try:
        Block.validate_block(genesis_block,bad_block)
    except Exception as ex:
        print(f'ERROR: {ex}')
if __name__=='__main__':
    main()