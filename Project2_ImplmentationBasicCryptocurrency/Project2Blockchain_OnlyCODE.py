
import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []  #The Chain
        self.current_transactions = [] #Currently trassaction
        self.new_block(previous_hash=1, proof=100) #Genesis Block
    def __str__(self) -> str:
        return f"""-The current transaction: {self.current_transactions}
-TheWhole Chain: {self.chain}"""

    def new_transaction(self, Transaction):
        self.current_transactions.append({
            "Sender": Transaction.sender,
            "Recipient": Transaction.recipient,
            "Amount transfered": Transaction.amount
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

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"{self.sender} sent {self.amount} to {self.recipient}"


if __name__ == "__main__":
    Nico_chain = Blockchain()    #Creation of the Blockchain
    transaction1 = Transaction('Nico','Nacho',89)
    Nico_chain.new_transaction(transaction1)
    Nico_chain.new_block(proof=1)
    valid = Nico_chain.valid_chain(Nico_chain.chain)
    print(valid)
    print(Nico_chain)