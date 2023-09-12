import os
import random
from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub()   

@app.route('/')
def route_mainpage():
    return 'Welcome to webpage'
@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.json_type())
@app.route('/blockchain/mining')
def route_miningBlocks():
    blockchain.add_block('NEW MINED BLOCK')
    print('new block added')
    return jsonify(blockchain.chain[-1].json_type())

PORT = 3107
if os.environ.get('PEER')=='True':
    PORT = random.randint(3107,4000)
app.run(port=PORT)

