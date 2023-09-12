import os
import random
from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)   

@app.route('/')
def route_mainpage():
    return 'Welcome to webpage'
@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.json_type())
@app.route('/blockchain/mining')
def route_miningBlocks():
    blockchain.add_block('NEW MINED BLOCK')
    added_block = blockchain.chain[-1]
    print('new block added')
    pubsub.broadcast_block(added_block)
    return jsonify(added_block.json_type())

PORT = 3107
if os.environ.get('PEER')=='True':
    PORT = random.randint(3107,4000)
app.run(port=PORT)

