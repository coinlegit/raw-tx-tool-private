########################
#redeem P2SH-P2WSH output
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
hash_inputs='46933a67dbb2492cb8ee4031eda0b6bd019f02c2bf05dba0bd78cc1fdb630325'
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
#redeeScript
scriptCode='52'+'21'+'03d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea0'+'21'+'02ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a'+'52'+'ae'
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

signed_tx=n_version+hashPrevouts+hashSequence+outpoint+witness_script+redeem_amount+sequence+hashOutputs+n_locktime+sig_hash_all
#print signed_tx

priv_key_1='cW9fNAfjiAryUkpTyWQRaLWGFVahTyRoiTgH8G259DZig8kJU2VB'
priv_key_1=wif_2_privkey(priv_key_1)
sk = SigningKey.from_string(binascii.unhexlify(priv_key_1), curve=SECP256k1)
sign_data_hash_d1=dhash256(signed_tx.decode('hex'))
#print 'sig_hash1:' + sign_data_hash_d1.encode('hex')
signature = sk.sign_digest_deterministic(sign_data_hash_d1, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
#print signature.encode('hex')

signature=signature.encode('hex')
sig_hash_type='01'
signature=signature+sig_hash_type
#print signature

p_len=(len(signature))/2
p_len=hex(p_len).lstrip('0x')
signature=p_len + signature
#print signature

priv_key_2='cQgY9UmyLWP5svEhCQYxKjnXDZct81BLjGgwKK3M16RaYNoHJV7p'
priv_key_2=wif_2_privkey(priv_key_2)
sk = SigningKey.from_string(binascii.unhexlify(priv_key_2), curve=SECP256k1)
sign_data_hash_d2=dhash256(signed_tx.decode('hex'))
#print 'sig_hash2:' + sign_data_hash_d2.encode('hex')
signature2 = sk.sign_digest_deterministic(sign_data_hash_d2, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
signature2=signature2.encode('hex')
sig_hash_type='01'
signature2=signature2+sig_hash_type
p_len=(len(signature2))/2
p_len=hex(p_len).lstrip('0x')
signature2=p_len + signature2

witness_02='04'
witness_item_1='00'
witness_item_2=signature
witness_item_3=signature2
witness_item_4=witness_script
witness_stack=witness_02+witness_item_1+witness_item_2+witness_item_3+witness_item_4
#redeem_public_key_hash='2322'+'0020b05313905066ffd001e4b7694dbfe2b5baae212c2f2665c78584e68da30ce90a'

#print n_version
#print segwit_marker
#print segwit_flag
#print n_inputs, hash_inputs, nth_inputs, redeem_public_key_hash, sequence
#print n_outputs, amount, pay_to_hash
#print witness_02, signature, redeem_public_key
#print n_locktime
final_sign_tx=n_version+segwit_marker+segwit_flag+n_inputs+hash_inputs+nth_inputs+redeem_public_key_hash+sequence+n_outputs+amount+pay_to_hash+witness_stack+n_locktime
print final_sign_tx

