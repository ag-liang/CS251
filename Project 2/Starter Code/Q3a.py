from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cRt42PFXwYRzLg1c2UCJiT45s87Gr759pRZq8t6Uybki5yM7D3bm')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cPrnhu921TPEB6qNzCokc3nKpVuVmB2JdmaRFrSknqErobVjdYan')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cVSYBhYCLvjGQxJSre25aV2EpZ355xdReKRZrGyCfzLCxxRvtPvh')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
    OP_2,                  
    my_public_key,         
    cust1_public_key,
    cust2_public_key,
    cust3_public_key,
    OP_4,                   
    OP_CHECKMULTISIG    
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00035 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '61ab2bfea0a88bf1037239b0d0a88654534851a07ccb9671e2d3cde7e04157a5')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
