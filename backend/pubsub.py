import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
#set up keys
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-d06d1b61-25b4-4db9-8776-119cae69fe80'
pnconfig.subscribe_key = 'sub-c-e4629177-04db-486c-84cb-78e5f56c65f3'
#pubnub client instance

TEST_CHANNEL ='TEST_CHANNEL'
#subcribe to channel
# create a class to add event-listener
class Listioner(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- incomming message block: {message_object}')

class PubSub():
    """
    Handles the publish/subcribe layer of the application
    Provide communications bw nodes and blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listioner())
    def publish(self,channel,message):
        """
        Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).syn()


def main():
    time.sleep(1)
    pubsub = PubSub()
    #publish to the channel
    pubsub.publish(TEST_CHANNEL,{'name':'Long'})

if __name__ == '__main__':
    main()
