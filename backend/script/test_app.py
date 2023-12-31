import requests
import time
from backend.wallet.wallet import Wallet
def get_blockchain():
    return requests.get('http://localhost:3107/blockchain').json()
def get_blockchain_mine():
    return requests.get('http://localhost:3107/blockchain/mining').json()
def post_transaction(recipient, amount):
    return requests.post('http://localhost:3107/wallet/transaction',json={'recipient':recipient, 'amount':amount}).json()
def get_wallet_info():
    return requests.get('http://localhost:3107/wallet/info').json()

start_blockchain = get_blockchain()
print(f'blockchain started: {start_blockchain}')

recipient = Wallet().address
transaction_post_1 = post_transaction(recipient,31)
print(f'\ntransaction_pos1: {transaction_post_1}')
time.sleep(1)
transaction_post_2 = post_transaction(recipient,31)
print(f'\ntransaction_pos2: {transaction_post_2}')

time.sleep(1)
mined_block = get_blockchain_mine()
print(f'\nnew mined_block: {mined_block}')

wallet_info = get_wallet_info()
print(f'\nWallet info: {wallet_info}')
