import hashlib
import binascii

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from  hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order
from  secp256k1 import GetUncompressedkey,GetPubkeyFromPrivkey

#pubkey
#827083A0162C03A27F5C23F9376404D60B818D09F841B20D32C9826CA6D9817E
#26EC871F76D7270220B1FF94A004FB3292FF41635A98D84A068863C94C8A0BEA

#$ cat msg.txt
#I like you yuka
#shasum -a 256 msg.txt  | awk '{print $1}'
#64d431be56e62f41e05a4af9dd662d4364878cce9e794ecbfcf56c311eabb68f

#the message signed to create signature
signed_msg='00'+'64d431be56e62f41e05a4af9dd662d4364878cce9e794ecbfcf56c311eabb68f'

#priv key for sign
#priv key
#echo -n yuka | sha256sum | awk '{print $1}'

priv_key='6552bcbf12684801a34bc52027b7eb39d67cc42195eddc710654f74f9c736f4e'
print priv_key
c_pub_key=GetPubkeyFromPrivkey( int(priv_key, 16) )
print c_pub_key
pub_key=GetUncompressedkey(c_pub_key)
print hex(pub_key[0])
print hex(pub_key[1])

sk = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
#create single hash256 of msg, in op_checkdatasig not double hash256
sign_data_hash=hash256(signed_msg.decode('hex'))
#create signature
signature = sk.sign_digest_deterministic(sign_data_hash, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
print signature.encode('hex')

#op_checkdatasig
#<sig> <msg> <pubKey> OP_CHECKDATASIG
#
#3045
#0221 00ad28f912f1240f59c646529d5b8e9a4d5185396478bfe4abdf5e7a87706879cb
#0220 46f649e1d3d09a30278d15e22f0f23a684b7ac1acaa75176eeb63733e7dc8aaa

