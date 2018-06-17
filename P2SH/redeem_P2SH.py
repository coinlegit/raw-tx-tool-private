########################
#redeem P2SH.py puzzle output
# ? + ? = 99
# because bitcoin-core not support this
# non normal transaction
# so must put scriptSig manual

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
hash_inputs='7da3ed20fd4ec8f38c34eecd141c3e6ed984ae072ada61acbe62fafb69fed4e2'
hash_inputs=reverse_byte_order(hash_inputs)
nth_inputs='00000000'

redeem_public_key_hash='3f58b4f7b14847a9083694b9b3b52a4cea2569ed'
#scriptPubKey='a914'+redeem_public_key_hash+'87'
#sequence
sequence='ffffffff'

#txouts
n_outputs='01'
amount=1.287
amount_satoshi=long(round(float(amount*__unit)))
amount=formatamount(amount_satoshi)
pay_to_hash='17'+'a914'+'3f58b4f7b14847a9083694b9b3b52a4cea2569ed'+'87'

redeem_amount=1.288
redeemScript='93016387'
# ? + ? = 99
#OP_ADD   93
#0x63     99
#OP_EQUAL 87
#0x62     98
scriptSig='51'+'0162'+'04'+redeemScript
print scriptSig
p_len=(len(scriptSig))/2
p_len=hex(p_len).lstrip('0x')
if int(p_len) < 10:
    p_len='0'+p_len

scriptSig=p_len+scriptSig
print scriptSig

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

final_sign_tx=n_version+n_inputs+hash_inputs+nth_inputs+scriptSig+sequence+n_outputs+amount+pay_to_hash+n_locktime
print final_sign_tx

#create it e8a9df4f3b5f5ff454ab96083fca8f8375359df26051ef2831bbc07e93788b27

