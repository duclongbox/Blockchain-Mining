from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_BLOCK

def test_blockchain_init():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_BLOCK['hash']
def test_addchain():
    blockchain = Blockchain()
    data = 'LONG'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == 'LONG'