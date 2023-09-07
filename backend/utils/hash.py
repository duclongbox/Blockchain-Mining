import hashlib
import json

def crypto_hash(*data): #*data create a tuple that allows to pass any data 
    """
    return a sha-256 hash of th given data 
    no matter the order of the input the hash function should return the same hashed value
    """
    #to encode every type of data
    stringified_data= sorted(map(lambda data: json.dumps(data),data)) 
    # print(f'stringified_data: {stringified_data}')
    joined_data= ''.join(stringified_data)
    # print(f'joined_data: {joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
# def stringify(data):
#     return json.dumps(data)
def main():
    print(f"crypto_hash('one',2,[3,'sdf']): {crypto_hash('one',[3,'sdf'],2)}")
    print(f"crypto_hash('one',2,[3,'sdf']): {crypto_hash('one',2,[3,'sdf'])}")
if __name__== '__main__':
    main()