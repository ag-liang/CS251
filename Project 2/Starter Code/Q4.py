from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script
######################################################################

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        OP_IF,
            OP_SHA256, hash_of_secret, OP_EQUALVERIFY,
            public_key_recipient, OP_CHECKSIG,
        OP_ELSE,
            OP_2, public_key_sender, public_key_recipient, OP_2, OP_CHECKMULTISIG,
        OP_ENDIF,
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    # recipient reveals x (the secret) and signs
    return [sig_recipient, secret, OP_TRUE]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    # both sender and recipient must sign
    return [OP_0, sig_sender, sig_recipient, OP_FALSE]
######################################################################

######################################################################
# Configured for your addresses
######################################################################

alice_txid_to_spend  = "3647322793812352301e7b9ae420d8cd45b391f1f0427e6233425c7036cc3914"
alice_utxo_index     = 0
alice_amount_to_send = 0.0015

bob_txid_to_spend    = "4bacb7e5c641d783091dffa08f1e6e0beee996a3e8f3ff7086a62f6f317b71a0"
bob_utxo_index       = 0
bob_amount_to_send   = 0.0003

btc_test3_chain_height = 1579945
bcy_test_chain_height  = 2548698

# Locktimes — Alice waits longer
alice_locktime = 5
bob_locktime   = 3

tx_fee = 0.0001

broadcast_transactions = False
alice_redeems = False
######################################################################
