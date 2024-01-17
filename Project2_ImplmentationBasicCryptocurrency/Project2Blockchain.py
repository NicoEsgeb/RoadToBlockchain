#PROJECT1: Simple Blockchain
import hashlib
import json
from time import time

#------------------------------Definition of the Blockchain Class---------------------------------
class Blockchain:
    #---------------------Definition of __init__ method-------------------------
    def __init__(self):
        #-----------------------self.chain=[]------------------------
        self.chain = []
        #------------------------------------------------------------

        #----------------self.current_transactions=[]----------------
        self.current_transactions = []
        #------------------------------------------------------------

        #----------------Creation fo Genesis blOCK-------------------
        self.new_block(previous_hash=1, proof=100)
        #------------------------------------------------------------
    #--------------------------------------------------------------------------




    #--------------------Deffinition of NEW_BLOCK method-----------------------
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.chain.append(block)
        #----------------------------------
        return block
        #----------------------------------
    #--------------------------------------------------------------------------


    #------------------------Method for visualization--------------------------
    def __str__(self) -> str:
        return f"""-The current transaction: {self.current_transactions}
-TheWhole Chain: {self.chain}"""
    #--------------------------------------------------------------------------



    #---------------------Definition of NEW_TRANSACTION method-----------------
    def new_transaction(self, sender, recipient, amount):
        """
        -This method creates a new transaction
        -3 Inputs:
            a- Sender: The sender of the money
            b- Recipient: The reciever of the money
            c- Amount: The amount of money that is going to be transfered
        """
        self.current_transactions.append({
        """
        -This ADDS the INPUT information to the self.current_transaction LIST
        -The information is added as a dictionary with the following 3 key-value pairs
        """
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1
        """
        -Return line: This lines takes the inthex of the last block in order to return
            the POSITION OF THE NEXT BLOCK in which this TRANSACTION is going to be ADDED

        -------OVERALL-------
        This method Does 3 things:
            1- It TAKES IN the DETAILS of a TRANSACTION.
            2- ADDS that transaction to a list of pending transactions
            3- Indicates that this transaction will be included in the next 
                block to be added to the blockchain. (Returning the INDEX)
        """
    #--------------------------------------------------------------------------



    #------------------Definition of HASH METHOD-------------------------------
    """
    This method is used to CREATE a HASH for a BLOCK
    """

    #-------DECORATOR-------------
    """
    -This DECORATOR indicates that this method is a STATIC METHOD which means it belongs
        to the BLOCKCHAIN CLASS ITSELF
    -This means you can call the method on the class itself, like this: Blockchain.hash(block),
        instead of having to create a Blockchain object to call the method.
    """
    @staticmethod
    #------Definition of method---
    """
    -Definition of the Method
    -The BLOCK parameter is the BLOCK that we want to HASH
    """
    def hash(block):
    #-----------------------------
    """
    -This line converts the block dictionary into a JSON string,
        sorts it by keys to ensure consistent ordering, and then 
        encodes it into bytes.
    -This is necessary because the hashlib.sha256 function requires 
        a bytes-like object as input.
    -SIMPLE EXPLANATION: We are telling the function which information use
        to CREATE the HASH (Everything inside the block and its key-value pairs)
    """
        block_string = json.dumps(block, sort_keys=True).encode()

    #-----------------------------
    """
    This is where the HASH is CREATED and returned it by the METHOD
    """
        return hashlib.sha256(block_string).hexdigest()

    #-----------------------------
    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]
    #-----------------------------



    #------------------Definition of Valid_Chain METHOD------------------------
    """
    This method is used to check fi the BlockChain is Valid
    """
    def valid_chain(self, chain):
        """
        -Chain parameter: Blockchain that we want to Validate
        """
        #-------------------
        last_block = chain[0]
        """
        -last_block = chain[0] This gets the first block of the Chain.
            IS THE STARTING POINT FOR THE VALIDATION
        """
        #-------------------
        current_index = 1
        """
        -This set the current index to 1 because we start the validation in the
            SECOND BLOCK. This is because the first Block is the "genesis" block
            and doesn't has a previous block to be check with.
        """
        #-------------------
        while current_index < len(chain):
            block = chain[current_index] #Block to be checked
            if block['previous_hash'] != self.hash(last_block):
                return False

            last_block = block
            current_index += 1

        return True

    #--------------------------------------------------------------------------



