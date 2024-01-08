import os
import requests
import random
from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.wallet.wallet import Wallet
from backend.wallet.transaction import Transaction
from backend.blockchain.blockchain import Blockchain
from backend.wallet.transaction_pool import TransactionPool
from backend.pubsub import PubSub

app = Flask(__name__)
CORS(app,resources={r'/*':{'origins':'http://localhost:3000'}})  #allow server not get block from browser
blockchain = Blockchain()
wallet = Wallet(blockchain)
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain,transaction_pool)   

@app.route('/')
def route_mainpage():
    return 'Welcome to webpage'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.json_type())

@app.route('/blockchain/range')
def route_blockchain_range():
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))
    
    return jsonify(blockchain.json_type()[::-1][start:end])

@app.route('/blockchain/length')
def route_blockchain_length():
    return jsonify(len(blockchain.chain))

@app.route('/blockchain/mining')
def route_miningBlocks():
    transaction_data = transaction_pool.transaction_query()
    transaction_data.append(Transaction.reward_transaction(wallet).json_type())
    blockchain.add_block(transaction_data)
    added_block = blockchain.chain[-1]
    print('new block added')
    pubsub.broadcast_block(added_block)
    transaction_pool.clear_transaction(blockchain)
    return jsonify(added_block.json_type())

@app.route('/wallet/transaction', methods =['POST'])
def wallet_transaction():
    transaction_fromUI = request.get_json()
    transaction  = transaction_pool.existed_transaction(wallet.address)
    if transaction:
       transaction.update_transaction(wallet,transaction_fromUI['recipient'],transaction_fromUI['amount'])
    else:
        transaction = Transaction(wallet,transaction_fromUI['recipient'],transaction_fromUI['amount'])
    
    pubsub.broadcast_transaction(transaction)
    print(f'transaction :  {transaction_pool.__dict__}')

    return jsonify(transaction.json_type())
@app.route('/wallet/info')
def wallet_information():
    return jsonify({'address':wallet.address, 'balance':wallet.balance})

@app.route('/transactions')
def route_transactions():
    return jsonify(transaction_pool.transaction_query())
    
    

ROOT_PORT = 3107
PORT = ROOT_PORT
if os.environ.get('PEER')=='True':
    PORT = random.randint(3107,4000)
    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    received_blockchain = Blockchain.deserialize(result.json())
    
    try:
        blockchain.replace_chain(received_blockchain.chain)
        print('Succesfully synchronized the local chain')
    except Exception as e :
        print(f'ERROR SYNCHROLIZE: {e}')
if os.environ.get('SEED_DATA')=='True':
    """
    Seeding data
    create each block with two transaction
    """
    for i in range(10):
        blockchain.add_block([
            Transaction(Wallet(),Wallet().address,random.randint(2,50)).json_type(),
            Transaction(Wallet(),Wallet().address,random.randint(2,50)).json_type()
        ])
    for i in range(3):
        transaction_pool.set_transaction(
            Transaction(Wallet(),Wallet().address,random.randint(2,50))
        )
        
app.run(port=PORT)

