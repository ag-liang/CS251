from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

A = 664
B = 8308

Q2a_txout_scriptPubKey = [
    OP_2DUP,     
    OP_ADD, A, OP_EQUALVERIFY,  
    OP_SUB, B, OP_EQUAL             
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00007 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '61ab2bfea0a88bf1037239b0d0a88654534851a07ccb9671e2d3cde7e04157a5')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
