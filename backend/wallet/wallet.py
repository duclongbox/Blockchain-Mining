import json
import uuid  #unique uni id

from backend.config import STARTING_BALACNCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.exceptions import InvalidSignature
class Wallet:
    """
    An individual wallet for a miner.
    Keeps track of the miner's balance
    Allows a miner to authorize transactions
    """
    def __init__(self):
        self.address = str(uuid.uuid4())[:8] 
        self.balance = STARTING_BALACNCE
        self.private_key = ec.generate_private_key(ec.SECP256K1(),default_backend) # 1st arg: specific eliptic cryptography standard,2nd : backend
        self.public_key = self.private_key.public_key()
        self.serialize_public_key()
    def sign(self,data):
        """
        create signature based on the data using private key 
        use sign method
        """
        #return a signature object  
        #signature return a unique byte string we need to use decode dss to transform to regular string
        return decode_dss_signature(self.private_key.sign(json.dumps(data).encode('utf-8')
        ,ec.ECDSA(hashes.SHA256())))  #2nd arg: EC digital signature algorithm
        
    def serialize_public_key(self):
        """
        convert public key to string serialize
        """
        #transform eliptic curve public key object to byte string
        self.public_key_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM, #(pem is common encoding in Security, with ---Begin...---End)
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.public_key = self.public_key_bytes.decode('utf-8') # bytes string to regular string
        
        
        
    @staticmethod
    def verify(public_key,data,signature):
        """
        verify the signature based on public key and original data
        """
        #deserialize the public key string to eliptic curve public class
        eliptic_curve_public = serialization.load_pem_public_key(
            public_key.encode('utf-8'), #encode back to byte string
            default_backend()
        )
        #signature return a tuple of 2 values
        (r,s) = signature
        
        try:
            eliptic_curve_public.verify(
                encode_dss_signature(r,s),
                json.dumps(data).encode('utf-8'),ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False 
        
def main():
    wallet = Wallet()
    print(f'wallet.__dict__  :  {wallet.__dict__}')
    
    data={'foo':'name'}
    signature = wallet.sign(data)
    print(f'signature: {signature}')
    
    valid_signature = wallet.verify(wallet.public_key,data,signature)
    print(f'valid: {valid_signature}')
    invalid_signature = wallet.verify(Wallet().public_key,data,signature)
    print(f'invalid: {invalid_signature}')
    
if __name__ == '__main__':
    main()