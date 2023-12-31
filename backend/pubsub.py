import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
#set up keys
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-d06d1b61-25b4-4db9-8776-119cae69fe80'
pnconfig.subscribe_key = 'sub-c-e4629177-04db-486c-84cb-78e5f56c65f3'
#pubnub client instance

CHANNELS = {
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}
#subcribe to channel
# create a class to add event-listener
class Listioner(SubscribeCallback):
    def __init__(self, blockchain,transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool
    def message(self, pubnub, message_object):
        print(f'\n-- channel: {message_object.channel} | Message: {message_object.message}')
        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.deserialize(message_object.message) # convert back to the Block-form
            new_chain = self.blockchain.chain[:] # create a copy of chain and then replace to validate the new chain
            new_chain.append(block)
            try:
                self.blockchain.replace_chain(new_chain) 
                self.transaction_pool.clear_transaction(self.blockchain)
                print('successfully replace a chain')
            except Exception as e:
                print(f'ERROR VALIDATE CHAIN: {e}')
        elif message_object.channel ==  CHANNELS['TRANSACTION']:
            transaction = Transaction.deserialize(message_object.message)
            self.transaction_pool.set_transaction(transaction) #clear the recorded transaction in block
            print(f'\n-- set new transaction to transaction pool ')
            
class PubSub():
    """
    Handles the publish/subcribe layer of the application
    Provide communications bw nodes and blockchain network.
    """
    def __init__(self, blockchain,transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listioner(blockchain,transaction_pool))
    def publish(self,channel,message):
        """
        Publish the message object to the channel
        """
        # self.pubnub.unsubscribe().channels(CHANNELS.values()).execute() # avoid redundant functionality
        self.pubnub.publish().channel(channel).message(message).sync()
        # self.pubnub.subscribe().channels(CHANNELS.values()).execute()

        
    def broadcast_block(self,block):
        """
        Broadcast a block object to nodes
        """
        self.publish(CHANNELS['BLOCK'],block.json_type()) #the publish contain the serialized json data 
    def broadcast_transaction(self,transaction):
        """
        Broadcast a transaction to all nodes
        """
        self.publish(CHANNELS['TRANSACTION'],transaction.json_type())
        

def main():
    pubsub = PubSub()
    time.sleep(1)

    #publish to the channel
    pubsub.publish(CHANNELS['BLOCK'],{'name':'Long'})

if __name__ == '__main__':
    main()
