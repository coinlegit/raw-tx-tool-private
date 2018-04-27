###################
#pay to public key
#redeem by signature
###################
import hashlib
import binascii

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order

__unit=100000000
sig_hash_all='01000000'
n_locktime='00000000'

segwit_marker='00'
segwit_flag='01'

#https://chain.so/tx/LTCTEST/7f52548e69bb4333fac3b24ba5a15e1b07bb5c803f07a78ee8a057c5c3846a75
#https://chain.so/tx/LTCTEST/580e534e24848e0c549996ba9255398225aa5bf02a616a51fc1d243f1234264e
#https://chain.so/tx/LTCTEST/11a4b11bc7af08a5770d6c5a1d2df15fb046d11b52cc5d704ad085789d664286
#txins
n_inputs='01'
hash_inputs='11fcb1c2c5a2ce9857b5b5a006af5a29b7b678c5affa9fbde1bc5beb2b77cd30'
hash_inputs=reverse_byte_order(hash_inputs)
#print hash_inputs
nth_inputs='00000000'

#sequence
sequence='ffffffff'

#txouts
n_outputs='01'
amount=2.99
#send to mgHpR4qokdVxPKfkpgZpJWx1WjAjsmnNze
amount_satoshi=long(round(float(amount*__unit)))
output_amount=formatamount(amount_satoshi)
#print output_amount
#output_amount='c051267700000000'
#pay_to_hash='001463b379dbf69f2ae27a96dba7418616c2d35faa15'
pay_to_hash='51bedd12781a10918b95ffa9975d77723385d5bbbf12301b755fc20a28da5355ac1ed5e72b7e63cec3b30e86ae95b55c7e076f72af1f77081c520a5b283f4ff4'
pay_to_hash='04'+pay_to_hash
p_len=(len(pay_to_hash))/2
p_len=hex(p_len).lstrip('0x')
pay_to_hash=p_len+pay_to_hash
pay_to_hash=pay_to_hash+'ac'
p_len=(len(pay_to_hash))/2
p_len=hex(p_len).lstrip('0x')
pay_to_hash=p_len+pay_to_hash

#this is inputs private key
priv_key='D4C85E8A20A87C27C81D3147AFD5A14D2734A30D67827AF9581E8D63230F6104'
#signed_tx=n_version+segwit_marker+segwit_flag+n_inputs+hash_inputs+nth_inputs+sequence+n_outputs+output_amount+pay_to_hash+sig_hash_all
redeem_public_key='03C14E197BFB58018F2399A59AD5301EFE786986F2D82E82BEC6234DEE155B0DFA'
redeem_public_key_hash=hash160(redeem_public_key.decode('hex')).encode('hex')
#19 #76 #a9 #88 #ac
#19 OP_DUP
#76 OP_PUSHDATA1
#a9 OP_HASH160
#88 OP_EQUALVERIFY
#ac OP_CHECKSIG

redeem_public_key_hash='1976a914'+redeem_public_key_hash+'88ac'
signed_tx=n_version+n_inputs+hash_inputs+nth_inputs + redeem_public_key_hash + sequence+n_outputs+output_amount+pay_to_hash+n_locktime+sig_hash_all
#print signed_tx
sk = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
#print sign_data_hash.encode('hex')
sign_data_hash_d2=dhash256(signed_tx.decode('hex'))
signature = sk.sign_digest_deterministic(sign_data_hash_d2, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
#print signature.encode('hex')

signature=signature.encode('hex')
sig_hash_type='01'
signature=signature+sig_hash_type

p_len=(len(signature))/2
p_len=hex(p_len).lstrip('0x')
signature=p_len + signature

#print signature
p_len=(len(redeem_public_key))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key=p_len+redeem_public_key
sig_pub=signature + redeem_public_key
p_len=(len(sig_pub))/2
p_len=hex(p_len).lstrip('0x')
sig_pub=p_len+sig_pub

#n_locktime
n_locktime='00000000'


final_sign_tx=n_version+n_inputs+hash_inputs+nth_inputs+sig_pub+sequence+n_outputs+output_amount+pay_to_hash+n_locktime
print final_sign_tx

