########################
#redeem P2PKH.py legacy output
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

########################
import hashlib
import binascii

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from  hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order
from key import wif_2_privkey

__unit=100000000
sig_hash_all='01000000'
n_locktime='00000000'

#n_version='02000000'
n_version='01000000'

#txins
n_inputs='01'
hash_inputs='b90d51d9e2acd91b0a0ad61f0729694699bff73239452392a70efc4d5b9958f8'
hash_inputs=reverse_byte_order(hash_inputs)
nth_inputs='00000000'

redeem_public_key_hash='ecebae831bbfbd7827542a82da4dc136e1288f71'
#previous txout scriptPubKey
scriptSig='1976a914'+redeem_public_key_hash+'88ac'
#sequence
sequence='ffffffff'

#txouts
n_outputs='01'
amount=0.99988480
amount_satoshi=long(round(float(amount*__unit)))
amount=formatamount(amount_satoshi)
#print output_amount
pay_to_hash='1976a914'+'ecebae831bbfbd7827542a82da4dc136e1288f71'+'88ac'

priv_key='cQuzMWdzbJezujAaAiMNq4Gr6zcFZt7BeD2VGUEN3LYBzZYgipRF'
priv_key=wif_2_privkey(priv_key)
redeem_public_key_hash='ecebae831bbfbd7827542a82da4dc136e1288f71'

redeem_amount=1.00000000
print "n_version   :",           n_version
print "n_inputs    :",           n_inputs
print "hash_inputs :",           hash_inputs
print "nth_inputs  :",           nth_inputs
print "scriptSig   :",           scriptSig
print "sequence    :",           sequence
print "n_outputs   :",           n_outputs
print "amount      :",           amount
print "scriptPubKey:",           pay_to_hash
print "n_locktime  :",           n_locktime
print "sig_hash_all:",           sig_hash_all


signed_tx=n_version+n_inputs+hash_inputs+nth_inputs+scriptSig+sequence+n_outputs+amount+pay_to_hash+n_locktime+sig_hash_all
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

redeem_public_key='02d7c9e36a4d31039d4b94a43246a4a5f0767f2f55ef9a359901c82c41fb1e4bff'
p_len=(len(redeem_public_key))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key=p_len+redeem_public_key

scriptSig=signature+redeem_public_key
p_len=(len(scriptSig))/2
p_len=hex(p_len).lstrip('0x')
scriptSig=p_len+scriptSig
#print scriptSig

final_sign_tx=n_version+n_inputs+hash_inputs+nth_inputs+scriptSig+sequence+n_outputs+amount+pay_to_hash+n_locktime
print final_sign_tx

