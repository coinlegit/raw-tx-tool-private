#!/usr/bin/env python

import hashlib
import binascii
import ecdsa

from  ecdsa.util import sigencode_der, sigencode_der_canonize, sigencode_strings
from  ecdsa.util import sigdecode_der, sigdecode_strings
from  ecdsa import SigningKey, NIST256p, SECP256k1
from  hash_util import hash256,dhash256,get_len_hex,formatamount,hash160,reverse_byte_order

from secp256k1 import GetUncompressedkey,ParseSignature

#the message for sign
signed_msg='0a00903a1a547ea6c0cb20b1ef2e3926202f27c4dee9a656a57d8a6800ce67e3'
print 'h_msg:', signed_msg
#priv key
priv_key='3b8407ec451a008c92c20068a6ca6e80e95c05b1a24655c646bcdadf33e8be2d'

sk = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
sign_data_hash_single=hash256(signed_msg.decode('hex'))
sign_data_hash_double=hash256(sign_data_hash_single)
print 'hash1:', sign_data_hash_single.encode('hex')
print 'hash2:', sign_data_hash_double.encode('hex')
#create signature
der = sk.sign_digest_deterministic(sign_data_hash_double, hashfunc=hashlib.sha256, sigencode=sigencode_der_canonize)
print 'der_s:',der.encode('hex')

#verify signature
pub_key='026225155bd431cbdd7e6d8ab07e61cd30482158b66fa11fe3c2492cd0a9dd2310'
(x, y) = GetUncompressedkey(pub_key)
x= hex(x)[2:].rstrip('L').zfill(64)
y= hex(y)[2:].rstrip('L').zfill(64)
pubkey_b=(x+y).decode('hex')
(sig_r,sig_s)=ParseSignature(der.encode('hex'))
print 'sig_r:', sig_r
print 'sig_s:', sig_s
signature=(sig_r+sig_s).lstrip('00').decode('hex')
vk = ecdsa.VerifyingKey.from_string(pubkey_b, curve=ecdsa.SECP256k1)
check=vk.verify(signature,  sign_data_hash_single, hashlib.sha256)
print 'check:', check



