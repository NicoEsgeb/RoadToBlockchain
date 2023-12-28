#PROJECT1: Simple Blockchain

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
        -The information is added as a dictionary with the following 3 ky-value pairs
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
        This method takes in the details of a transaction, adds that 
        transaction to a list of pending transactions, and then indicates that this transaction 
        will be included in the next block to be added to the blockchain.
        """
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]


