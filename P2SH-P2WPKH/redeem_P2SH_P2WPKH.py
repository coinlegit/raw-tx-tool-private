##################################
#redeem P2SH_P2WPKH segwit example
#
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

####################################
import hashlib
import binascii

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order
from key import wif_2_privkey

__unit=100000000
sig_hash_all='01000000'
#n_locktime='92040000'
n_locktime='00000000'


#n_version='02000000'
n_version='01000000'
segwit_marker='00'
segwit_flag='01'

#txins
n_inputs='01'
hash_inputs='b9c0b0bee666eb3b53ea501271c168da9a6a0527b66bfc87d8f1cbc5b1d7a2de'
hash_inputs=reverse_byte_order(hash_inputs)
nth_inputs='00000000'
outpoint=hash_inputs+nth_inputs
#hash outpoint=prev_tx_id+nth
hashPrevouts=dhash256(outpoint.decode('hex')).encode('hex')

#sequence
sequence='ffffffff'
hashSequence=dhash256(sequence.decode('hex')).encode('hex')

#txouts
n_outputs='01'
amount=1.2999
amount_satoshi=long(round(float(amount*__unit)))
amount=formatamount(amount_satoshi)
#print output_amount
pay_to_hash='1976a914'+'ecebae831bbfbd7827542a82da4dc136e1288f71'+'88ac'
outputs=amount+pay_to_hash
#amount+dest_script
hashOutputs=dhash256(outputs.decode('hex')).encode('hex')

priv_key='cQuzMWdzbJezujAaAiMNq4Gr6zcFZt7BeD2VGUEN3LYBzZYgipRF'
priv_key=wif_2_privkey(priv_key)

redeem_public_key_hash='c712299cbd34980b0d6b2dee8fe9a11fa816999e'
scriptCode='17160014'+redeem_public_key_hash
#scriptCode='1976a914'+redeem_public_key_hash+'88ac'
#scriptCode='17a914'+redeem_public_key_hash+'87'

redeem_amount=1.3
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

signed_tx=n_version+hashPrevouts+hashSequence+outpoint+scriptCode+redeem_amount+sequence+hashOutputs+n_locktime+sig_hash_all
#print signed_tx
sk = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
sign_data_hash_d2=dhash256(signed_tx.decode('hex'))
print reverse_byte_order(sign_data_hash_d2.encode('hex'))
signature = sk.sign_digest_deterministic(sign_data_hash_d2, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
#print signature.encode('hex')

signature=signature.encode('hex')
sig_hash_type='01'
signature=signature+sig_hash_type

#print signature
p_len=(len(signature))/2
p_len=hex(p_len).lstrip('0x')
signature=p_len + signature

#print signature

redeem_public_key='03302537fa9e3648ddbae25c068714c842b2540a1e9a5b3e38c628ba7471d33fa4'
p_len=(len(redeem_public_key))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key=p_len+redeem_public_key
witness_02='02'

redeem_public_key_hash=scriptCode

#print n_version
#print segwit_marker
#print segwit_flag
#print n_inputs, hash_inputs, nth_inputs, redeem_public_key_hash, sequence
#print n_outputs, amount, pay_to_hash
#print witness_02, signature, redeem_public_key
#print n_locktime
final_sign_tx=n_version+segwit_marker+segwit_flag+n_inputs+hash_inputs+nth_inputs+redeem_public_key_hash+sequence+n_outputs+amount+pay_to_hash+witness_02+signature+redeem_public_key+n_locktime
print final_sign_tx

