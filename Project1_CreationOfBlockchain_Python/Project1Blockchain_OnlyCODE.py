
import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []  #The Chain
        self.current_transactions = [] #Currently trassaction that is going to be added to the next block
        self.new_block(previous_hash=1, proof=100) #Genesis Block
    def __str__(self) -> str:
        return f"""-The current transaction: {self.current_transactions}
-TheWhole Chain: {self.chain}"""

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]


    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False

            last_block = block
            current_index += 1

        return True

if __name__ == "__main__":
    Nico_chain = Blockchain()    #Creation of the Blockchain 
    Nico_chain.new_transaction('Nico', 'Nacho', 77) #Creation of New Transaction
    Nico_chain.new_transaction("Nico","Aniet",99)
    Nico_chain.new_block(proof=1)
    print(Nico_chain)
    valid = Nico_chain.valid_chain(Nico_chain.chain)
    print(valid)
