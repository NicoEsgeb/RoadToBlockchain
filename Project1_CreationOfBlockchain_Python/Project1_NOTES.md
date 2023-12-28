
----------------------------------What do I know already?-----------------------------------

-Blockchain is essentially a chain of Blockch, in which each block contains some data. In the case of Bitcoin, Ethereum, Solana, etc..
the data is a list of transactions. Blockchain is MORE than that, it can contain bassically any type of information.

-------------------------------Wide view about this first small project-----------------------------------------

I need to answer the question "What I am going to do now?"

The answer is:

1-Using python to build a small and simple blockchain


----------------------------------Let's talk about that code-----------------------------------
I need to now "How I am going to do it?"

The answers are:

1-Define the Blockchain Class:

    /Blockchain Class: Main structure that will hold the Blockchain

    /It has 2 main parts:

        a- The chain itself (a list of blocks)

        b- The current transactions (List of transactions that will be added to the next block)


2-METHOD A: Create new transactions:

    /Method that allows to add new transactions to the blockchain

    /These transactions will be included in the next block mined

    /Transaction: Transfer of coins(tokens) from one account to another


3-METHOD B: Create new Blocks:

    /This method allows to add new blocks to the blockchain

    /Each block will include: 

        a-Current list of transactions

        b-timestamp

        c-Reference to the previous block in the chain (This is what makes the chain a CHAIN)


4-METHOD C: Hash Blocks:

    /This metho Takes one block as an input and return a hash(Unique Number)


5-METHOD D: Validate the Chain:

    /This method will check the integrity of the entire block
    /How does it work? It goes to each block and it makes sure that the reference of the previous Block
        matches the hash of that block. If this references doesn't match, we know that the blockchain has been tampered.