
'''
keep track how much time to mine a block
tracking the difficulty adjustment 
'''

import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SEC

blockchain = Blockchain()
times = []

for i in range(100):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()
    calculate_time = (end_time - start_time)/SEC
    times.append(calculate_time)
    average_time = sum(times)/(len(times))
    print(f'New mined Block difficulty : {blockchain.chain[-1].difficulty}')
    print(f'mining time : {calculate_time}')
    print(f'Average of time: {average_time}\n')
