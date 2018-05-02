########################
#pay to witness_v0_keyhash
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

__unit=100000000
sig_hash_all='01000000'
#n_locktime='92040000'
n_locktime='00000000'

#$ bash cli.bash  validateaddress tltc1qvwehnklknu4wy75kmwn5rpskctf4l2s4cfd48r
#{
#  "isvalid": true,
#  "address": "tltc1qvwehnklknu4wy75kmwn5rpskctf4l2s4cfd48r",
#  "scriptPubKey": "001463b379dbf69f2ae27a96dba7418616c2d35faa15",
#  "ismine": true,
#  "iswatchonly": false,
#  "isscript": false,
#  "iswitness": true,
#  "witness_version": 0,
#  "witness_program": "63b379dbf69f2ae27a96dba7418616c2d35faa15",
#  "pubkey": "025f647b87ecd3674122b41a87750e56dba95e49ff52f102cd28bd25dd94068962",
#  "timestamp": 1523762634,
#  "hdkeypath": "m/0'/0'/15'",
#  "hdmasterkeyid": "5354b09b4a0d665e1c884ba429ac91a34c7aac1c"
#}


n_version='02000000'
segwit_marker='00'
segwit_flag='01'

#txins
n_inputs='01'
#hash_inputs='8619593e5f2ef047bdb9d451d6e07b9e956e59c1335cd65010c6d4085fdcf397'
hash_inputs='40fa1c89158d99cec5bb5601d128adf5d99af9b2a3201785d53eae92d19d1de2'
hash_inputs=reverse_byte_order(hash_inputs)
nth_inputs='00000000'
outpoint=hash_inputs+nth_inputs
#hash outpoint=prev_tx_id+nth
hashPrevouts=dhash256(outpoint.decode('hex')).encode('hex')

nth_inputs_00='00'

#sequence
#sequence='feffffff'
sequence='ffffffff'
hashSequence=dhash256(sequence.decode('hex')).encode('hex')

#txouts
n_outputs='01'
amount=2.978
#send to mgHpR4qokdVxPKfkpgZpJWx1WjAjsmnNze
amount_satoshi=long(round(float(amount*__unit)))
amount=formatamount(amount_satoshi)
#print output_amount
pay_to_hash='1976a914'+'7ece5d01d1477b825f2e226511b8f4fc870048d2'+'88ac'
outputs=amount+pay_to_hash
#amount+dest_script
hashOutputs=dhash256(outputs.decode('hex')).encode('hex')


priv_key='bfb66ca975dd57d65953a809857cb7df3c3e517824f97e8440573d66768ab7b3'
redeem_public_key_hash='0d6d184ef4430e7b903e440f475c8ceaf408eb0e'
scriptCode='17a914'+redeem_public_key_hash+'87'

#redeem_public_key_hash='63b379dbf69f2ae27a96dba7418616c2d35faa15'
#scriptCode='17160014'+redeem_public_key_hash

#print redeem_public_key_hash
#signed_tx=n_version+hashPrevouts+hashSequence+outpoint+redeem_public_key_hash+amount+sequence+hashOutputs+n_locktime+sig_hash_all
redeem_amount=2.979
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

#send to mgHpR4qokdVxPKfkpgZpJWx1WjAjsmnNze
amount_satoshi=long(round(float(redeem_amount*__unit)))
redeem_amount=formatamount(amount_satoshi)

signed_tx=n_version+hashPrevouts+hashSequence+outpoint+scriptCode+redeem_amount+sequence+hashOutputs+n_locktime+sig_hash_all
#signed_tx=n_version+hashPrevouts+hashSequence+outpoint+amount+sequence+hashOutputs+n_locktime+sig_hash_all
#print signed_tx
sk = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
sign_data_hash_d2=dhash256(signed_tx.decode('hex'))
print sign_data_hash_d2.encode('hex')
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

#redeem_public_key='001463b379dbf69f2ae27a96dba7418616c2d35faa15'
redeem_public_key='025f647b87ecd3674122b41a87750e56dba95e49ff52f102cd28bd25dd94068962'
p_len=(len(redeem_public_key))/2
p_len=hex(p_len).lstrip('0x')
redeem_public_key=p_len+redeem_public_key
witness_02='02'
#sig_pub=signature+redeem_public_key

#n_locktime
#n_locktime='92040000'

#redeem_public_key_hash='171600'+redeem_public_key_hash
#redeem_public_key_hash='00'
redeem_public_key_hash=scriptCode
print redeem_public_key_hash[2:4]
if redeem_public_key_hash[4:6] == '00':
    redeem_public_key_hash='00'

print n_version
print segwit_marker
print segwit_flag
print n_inputs, hash_inputs, nth_inputs, redeem_public_key_hash, sequence
print n_outputs, amount, pay_to_hash
print witness_02, signature, redeem_public_key
print n_locktime
#final_sign_tx=n_version+segwit_marker+segwit_flag+n_inputs+hash_inputs+nth_inputs+redeem_public_key_hash+sequence+n_outputs+amount+pay_to_hash+witness_02+signature+redeem_public_key+n_locktime
final_sign_tx=n_version+segwit_marker+segwit_flag+n_inputs+hash_inputs+nth_inputs+redeem_public_key_hash+sequence+n_outputs+amount+pay_to_hash+witness_02+signature+redeem_public_key+n_locktime
print final_sign_tx

#sended tx 0946ebdc606e49013b497a31c9118e5b0d91ed78c03df9a3f94a58a9958ac120

