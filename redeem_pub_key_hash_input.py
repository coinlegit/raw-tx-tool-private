########################
#pay to public key hash
#redeem by signature + public key
########################
import hashlib
import binascii

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order

__unit=100000000
sig_hash_all='01000000'
n_locktime='00000000'

n_version='02000000'
segwit_marker='00'
segwit_flag='01'

#txins
n_inputs='01'
hash_inputs='8619593e5f2ef047bdb9d451d6e07b9e956e59c1335cd65010c6d4085fdcf397'
hash_inputs=reverse_byte_order(hash_inputs)
#print hash_inputs
nth_inputs='00000000'

#sequence
sequence='ffffffff'

#txouts
n_outputs='01'
amount=2.98
#send to mgHpR4qokdVxPKfkpgZpJWx1WjAjsmnNze
amount_satoshi=long(round(float(amount*__unit)))
output_amount=formatamount(amount_satoshi)
#print output_amount
pay_to_hash='1976a914'+'7ece5d01d1477b825f2e226511b8f4fc870048d2'+'88ac'


priv_key='7b84df24745e75e026179334c6220efd080c667351b5f4b2f7cd95934908fe64'
#19 #76 #a9 #88 #ac
#19 OP_DUP
#76 OP_PUSHDATA1
#a9 OP_HASH160
#88 OP_EQUALVERIFY
#ac OP_CHECKSIG

redeem_public_key_hash='0451bedd12781a10918b95ffa9975d77723385d5bbbf12301b755fc20a28da5355ac1ed5e72b7e63cec3b30e86ae95b55c7e076f72af1f77081c520a5b283f4ff4'
p_len=(len(redeem_public_key_hash))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key_hash=p_len+redeem_public_key_hash
redeem_public_key_hash=redeem_public_key_hash+'ac'
p_len=(len(redeem_public_key_hash))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key_hash=p_len+redeem_public_key_hash
#print redeem_public_key_hash
signed_tx=n_version+n_inputs+hash_inputs+nth_inputs + redeem_public_key_hash + sequence+n_outputs+output_amount+pay_to_hash+n_locktime+sig_hash_all
#print signed_tx
sk = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
#print sign_data_hash.encode('hex')
sign_data_hash_d2=dhash256(signed_tx.decode('hex'))
#print sign_data_hash_d2.encode('hex')
signature = sk.sign_digest_deterministic(sign_data_hash_d2, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
#print signature.encode('hex')

signature=signature.encode('hex')
sig_hash_type='01'
signature=signature+sig_hash_type

p_len=(len(signature))/2
p_len=hex(p_len).lstrip('0x')
#print p_len
signature=p_len + signature

sig_pub=signature
p_len=(len(sig_pub))/2
p_len=hex(p_len).lstrip('0x')
sig_pub=p_len+sig_pub

#n_locktime
n_locktime='00000000'


final_sign_tx=n_version+n_inputs+hash_inputs+nth_inputs+sig_pub+sequence+n_outputs+output_amount+pay_to_hash+n_locktime
print final_sign_tx

