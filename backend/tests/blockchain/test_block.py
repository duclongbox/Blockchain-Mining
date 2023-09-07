import time
from backend.blockchain.block import Block, GENESIS_BLOCK
from backend.config import MINE_RATE,SEC
def test_mine_block():
    first_block = Block.genesis()
    data = 'LONG'
    next_block = Block.mine_block(first_block,data)

    assert isinstance(next_block,Block)
    assert isinstance(first_block,Block)

def test_genesis_block():
    genesis = Block.genesis()
    assert isinstance(genesis,Block)
    for key,value in GENESIS_BLOCK.items():
        getattr(genesis,key) == value
    
def test_quickly_mining_block():
    last_block = Block.mine_block(Block.genesis(), 'CHAY')
    next_mined_block = Block.mine_block(last_block,'IUU')
    assert next_mined_block.difficulty == last_block.difficulty+1
def test_slowly_mining_block():
    last_block = Block.mine_block(Block.genesis(), 'CHAY')
    time.sleep(MINE_RATE/SEC)  #note: time.sleep take the second as unit, convert to second 
    next_mined_block = Block.mine_block(last_block,'IUU')
    assert next_mined_block.difficulty == last_block.difficulty-1
