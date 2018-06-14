########################
#redeem P2SH-P2WSH output
#redeem non-standard script
#send to OP_RETURN
#redeem by witness program
#Double SHA256 of the serialization of:
#^     1. nVersion of the transaction (4-byte little endian)
#      2. hashPrevouts (32-byte hash)
#      3. hashSequence (32-byte hash)
#^     4. outpoint (32-byte hash + 4-byte little endian)
#      5. scriptCode of the input (serialized as scripts inside CTxOuts)
#      6. value of the output spent by this input (8-byte little endian)
#^     7. nSequence of the input (4-byte little endian)
#      8. hashOutputs (32-byte hash)
#^     9. nLocktime of the transaction (4-byte little endian)
#^    10. sighash type of the signature (4-byte little endian)

########################
import hashlib
import binascii

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order
from key       import wif_2_privkey

__unit=100000000
sig_hash_all='01000000'
n_locktime='00000000'

n_version='02000000'
segwit_marker='00'
segwit_flag='01'

#txins
n_inputs='01'
hash_inputs='be6c81f1b184c242d8c70a051264d6281183a9cf603742490ce7f129c48f1465'
hash_inputs=reverse_byte_order(hash_inputs)
nth_inputs='00000000'
outpoint=hash_inputs+nth_inputs
#hash outpoint=prev_tx_id+nth
hashPrevouts=dhash256(outpoint.decode('hex')).encode('hex')

#sequence
sequence='ffffffff'
hashSequence=dhash256(sequence.decode('hex')).encode('hex')

#txouts
n_outputs='02'
amount=0.0
amount_satoshi=long(round(float(amount*__unit)))
amount=formatamount(amount_satoshi)
#print output_amount
#pay_to_hash='1976a914'+'ecebae831bbfbd7827542a82da4dc136e1288f71'+'88ac'
pay_to_hash='0d'+'6a'+'0b'+'70617373696f6e6f667663'
outputs=amount+pay_to_hash

amount2=1.2999
amount_satoshi2=long(round(float(amount2*__unit)))
amount2=formatamount(amount_satoshi2)
pay_to_hash2='1976a914'+'ecebae831bbfbd7827542a82da4dc136e1288f71'+'88ac'
output2=amount2+pay_to_hash2

#amount+dest_script
hashOutputs=dhash256(outputs.decode('hex')).encode('hex')
#redeeScript
scriptCode='020203040569696969'
witness_script=scriptCode
p_len=(len(witness_script))/2
p_len=hex(p_len).lstrip('0x')
witness_script=p_len+witness_script

#hash256(redeemScript)
redeem_public_key_hash=hash256(scriptCode.decode('hex')).encode('hex')
redeem_public_key_hash='0020'+redeem_public_key_hash
p_len=(len(redeem_public_key_hash))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key_hash=p_len + redeem_public_key_hash
p_len=(len(redeem_public_key_hash))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key_hash=p_len + redeem_public_key_hash
print redeem_public_key_hash

redeem_amount=1.30000000
print "n_version   :",           n_version
print "hashPrevouts:",           hashPrevouts
print "hashSequence:",           hashSequence
print "outpoint    :",           outpoint
print "scriptCode  :",           scriptCode
print "redeem_amount:",          redeem_amount
print "sequence    :",           sequence
print "hashOutputs :",           hashOutputs
print "n_locktime  :",           n_locktime
print "sig_hash_all:",           sig_hash_all

amount_satoshi=long(round(float(redeem_amount*__unit)))
redeem_amount=formatamount(amount_satoshi)

witness_02='01'
witness_item_1='09'+'020203040569696969'
witness_stack=witness_02+witness_item_1

#print n_version
#print segwit_marker
#print segwit_flag
#print n_inputs, hash_inputs, nth_inputs, redeem_public_key_hash, sequence
#print n_outputs, amount, pay_to_hash
#print witness_02, signature, redeem_public_key
#print n_locktime
final_sign_tx=n_version+segwit_marker+segwit_flag+n_inputs+hash_inputs+nth_inputs+redeem_public_key_hash+sequence+n_outputs+amount+pay_to_hash+output2+witness_stack+n_locktime
print final_sign_tx

#https://chain.so/tx/BTCTEST/5752f08bdd18a71c4456b5904646584e414077ea2c3ab2a9895a0c38305444ad

