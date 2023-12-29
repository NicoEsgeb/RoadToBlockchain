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
        """
        -This list act as the BLOCKCHAIN ITSELF
        -The BLOCKS are going to be STORED in this list
        -Every ELEMENT in this list is going to be a BLOCK
        -As we know, evry BLOCK is going to be a collection of DATA
        """
        #------------------------------------------------------------

        #----------------self.current_transactions=[]----------------
        self.current_transactions = []
        """
        -This LIST holds the CURRENT TRANSACTION that has not been added
            to a block yet
        -How does this work?
            1-When a NEW TRANSACTION IS CREATED, is ADDED to this lIST
            2-When a NEW BLOCK IS CREATED:
                a-All the INFORMATION in this LIST is ADDED to that BLOCK
                b-The LIST is CLEARED
            3-OVERALL, this list HOLDS the information of the next BLOCK 
                that is going to be mined
        """
        #------------------------------------------------------------
    #--------------------------------------------------------------------------




    #--------------------Deffinition of NEW_BLOCK method-----------------------
    """
    This method is used to CREATE a NEW BLOCK and ADD it to the BLOCKCHAIN(self.chain)
    """
    def new_block(self, proof, previous_hash=None):
        """
        1-Parameters:
        a-proof: Proof that some work has been done
        b-previous_hash: The hash os the previous Block
        """

        """
        The following variable is the creation of a "block" as a Dictionary
        with their respectives key-value pairs:
            a-index: The index of the New Block. This is one more than the
                number of blocks in the currently chain
            b-timestamp: The current time in which the Block was created
            c-transactions: The list of transactions that are going to be included 
                in the new Block
            d-proof: The proof of work for this Block
            e-previoous_hash: The Hash of the previous Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #----------------------------------
        """
        This lines reset the List of transactions after adding the information to
        the new_block dictonary
        """
        #----------------------------------
        """
        This lines creates add the new block created to the Chain
        """
        self.chain.append(block)
        #----------------------------------
        """
        This lines return the new block(dictionary) created
        """
        return block
        #----------------------------------
        """
        Overall:
        This Method:
            1-Takes in DETAILS of the NEW BLOCK
            2-Adds that NEW BLOCK to the BLOCKCHAIN
            3-CLEAR the CURRENT TRANSACTIONS for the NEXT BLOCK
        """
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


