#!/usr/bin/env python3

'''
##--事例1--##
step 1:
stack -> 0x00 (OP_0)

step 2:
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001

step 3:
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x5141042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf51ae

step 4:  0xa9 (OP_HASH160)
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x5141042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf51ae,
         0xe9c3dd0c07aac76179ebc76a6c78d4d67c6c160a

step 5:  0x14 (pushdata 20 bytes) 0xe9c3dd0c07aac76179ebc76a6c78d4d67c6c160a
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x5141042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf51ae,
         0xe9c3dd0c07aac76179ebc76a6c78d4d67c6c160a,
         0xe9c3dd0c07aac76179ebc76a6c78d4d67c6c160a

step 6:  87 OP_EQUAL
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x5141042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf51ae,
         0x01

step 7:  0x51 (OP_1)
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x01

step 8: 0x41 (Pushdata 65 bytes) 042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x01,
         0x042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf

step 9: 0x51 (OP_1)
stack -> 0x00,
         0x3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001,
         0x01,
         0x042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf,
         0x01

step 10: 0xae (OP_CHECKMULTISIG)
         We have 1 sig and 1 pubkey. To check multisig we need to get transaction which was signed. We will come back to this step once we have transaction which was signed.


#Parse Signature:
0x30 DER
0x45 Length
0x02 Type Integer
0x21 Length of r
0x00 (ignore) ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf883 (r)
0x02 Type Integer
0x20 Length of s
     0b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b790 (s)
0x01 SIGHASH_ALL

#r||s [1]
ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf883 0b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b790

##Parsing raw transaction of unlocking script

01 00 00 00  #Version
01           #input count
c8 cc 2b 56 52 5e 73 4f f6 3a 13 bc 6a d0 6a 9e 56 64 df 8c 67 63 22 53 a8 e3 60 17 ae e3 ee 40 #Previous transaction
00 00 00 00 #Previous transaction out index
--------- replace this [
90
00 48 30 45 02 21 00 ad 08 51 c6 9d d7 56 b4 51
90 b5 a8 e9 7c b4 ac 3c 2b 0f a2 f2 aa e2 3a ed
6c a9 7a b3 3b f8 83 02 20 0b 24 85 93 ab c1 25
95 12 79 3e 7d ea 61 03 6c 60 17 75 eb b2 36 40
a0 12 0b 0d ba 2c 34 b7 90 01 45 51 41 04 2f 90
07 4d 7a 5b f3 0c 72 cf 3a 8d fd 13 81 bd bd 30
40 70 10 e8 78 f3 a1 12 69 d5 f7 4a 58 78 85 05
cd ca 22 ea 6e ab 7c fb 40 dc 0e 07 ab a2 00 42
4a b0 d7 91 22 a6 53 ad 0c 7e c9 89 6b df 51 ae
------------- ]
fe ff ff ff             #sequence
01                      #out count
20 f4 0e 00 00 00 00 00 #value
19                      #script size
76 a9 14 1d 30 34 20 95 96 1d 95 1d 30 68 45 ef 98 ac 08 47 4b 36 a0 88 ac #script pubkey hash
a7 27 04 00             #lock time
---> Add SIGHASH_ALL here

###########################################
#replace unlocking script (scriptSig) by previous scriptPubkey[p2pkh]
#replace unlocking script (scriptSig) by redeemScript [p2sh]
01 00 00 00 #Version
01          #input count
c8 cc 2b 56 52 5e 73 4f f6 3a 13 bc 6a d0 6a 9e 56 64 df 8c 67 63 22 53 a8 e3 60 17 ae e3 ee 40 Previous transaction
00 00 00 00 #Previous transaction out index
------- locking script [
#17 a914e9c3dd0c07aac76179ebc76a6c78d4d67c6c160a87
#redeemscript/scriptpubkey
------- ]
fe ff ff ff #sequence
01          #out count
20 f4 0e 00 00 00 00 00 value
19          #script size
76 a9 14 1d 30 34 20 95 96 1d 95 1d 30 68 45 ef 98 ac 08 47 4b 36 a0 88 ac
a7 27 04 00 #lock time
01 00 00 00 SIGHASH_ALL

###get redeemScript from unlocking script##############
90 #Length of scriptSig
00 #OP_0
48 #Length of Signature
30 45
02 21 00 ad 08 51 c6 9d d7 56 b4 51 90 b5 a8 e9 7c b4 ac 3c 2b 0f a2 f2 aa e2 3a ed 6c a9 7a b3 3b f8 83
02 20    0b 24 85 93 ab c1 25 95 12 79 3e 7d ea 61 03 6c 60 17 75 eb b2 36 40 a0 12 0b 0d ba 2c 34 b7 90
01 SIGHASH_ALL
------ Redeem script ---->
45 51 41 04 2f 90
07 4d 7a 5b f3 0c 72 cf 3a 8d fd 13 81 bd bd 30
40 70 10 e8 78 f3 a1 12 69 d5 f7 4a 58 78 85 05
cd ca 22 ea 6e ab 7c fb 40 dc 0e 07 ab a2 00 42
4a b0 d7 91 22 a6 53 ad 0c 7e c9 89 6b df 51 ae
<-------------------------

#sig-hash
01 00 00 00 #Version
01          #input count
c8 cc 2b 56 52 5e 73 4f f6 3a 13 bc 6a d0 6a 9e 56 64 df 8c 67 63 22 53 a8 e3 60 17 ae e3 ee 40 Previous transaction
00 00 00 00 #Previous transaction out index
------ Redeem script ---->
45 51 41 04 2f 90
07 4d 7a 5b f3 0c 72 cf 3a 8d fd 13 81 bd bd 30
40 70 10 e8 78 f3 a1 12 69 d5 f7 4a 58 78 85 05
cd ca 22 ea 6e ab 7c fb 40 dc 0e 07 ab a2 00 42
4a b0 d7 91 22 a6 53 ad 0c 7e c9 89 6b df 51 ae
<-------------------------
fe ff ff ff #sequence
01          #out count
20 f4 0e 00 00 00 00 00 #value
19          #script size
76 a9 14 1d 30 34 20 95 96 1d 95 1d 30 68 45 ef 98 ac 08 47 4b 36 a0 88 ac
a7 27 04 00 #lock time
01 00 00 00 SIGHASH_ALL

#raw-tx sig-hash [2]
#dhash256(sig-hash)
0x0100000001c8cc2b56525e734ff63a13bc6ad06a9e5664df8c67632253a8e36017aee3ee4000000000455141042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf51aefeffffff0120f40e00000000001976a9141d30342095961d951d306845ef98ac08474b36a088aca727040001000000

#public-key[3]
#04 uncompressed
0x042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf
0x2f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf

'''
import ecdsa
from secp256k1 import GetUncompressedkey,ParseSignature
import hashlib
import binascii

#sig_b[1]
#pubkey_b[3]
#raw_txn_b[2]
def sigcheck(sig_b: bytes, pubkey_b: bytes, raw_txn_b: bytes):
    txn_sha256_b = hashlib.sha256(raw_txn_b).digest()
    prefix = pubkey_b[0:1]
    #print('prefix = %s' % prefix)
    #print('input pubkey = %s' % bytes.decode(binascii.hexlify(pubkey_b)))
    if prefix == b'\x02' or prefix == b'\x03':
        pubkey_b = GetUncompressedkey(pubkey_b)[1:]
    elif prefix == b'\x04':
        pubkey_b = pubkey_b[1:]
    try:
        #print("full public key = %s" % bytes.decode(binascii.hexlify(pubkey_b)))
        vk = ecdsa.VerifyingKey.from_string(pubkey_b, curve=ecdsa.SECP256k1)
        if vk.verify(sig_b, txn_sha256_b, hashlib.sha256) == True:
            print('valid')
            return True
        else:
            print('sigcheck: invalid')
            return False
    except ecdsa.BadSignatureError:
        print('sigcheck: Bad Signature')
        return False

def sigcheck2(sig_b: bytes, pubkey_b: bytes, raw_txn_256_b: bytes):
    txn_sha256_b = raw_txn_256_b
    prefix = pubkey_b[0:1]
    #print('prefix = %s' % prefix)
    #print('input pubkey = %s' % bytes.decode(binascii.hexlify(pubkey_b)))
    if prefix == b'\x02' or prefix == b'\x03':
        pubkey_b=binascii.hexlify(pubkey_b)
        pubkey_b = GetUncompressedkey(pubkey_b)
        uncompressed_key = hex(pubkey_b[0])[2:].zfill(64) + hex(pubkey_b[1])[2:].zfill(64)
        #print (uncompressed_key)
        pubkey_b=binascii.unhexlify(uncompressed_key)
    elif prefix == b'\x04':
        pubkey_b = pubkey_b[1:]
    try:
        #print("full public key = %s" % bytes.decode(binascii.hexlify(pubkey_b)))
        vk = ecdsa.VerifyingKey.from_string(pubkey_b, curve=ecdsa.SECP256k1)
        if vk.verify(sig_b, txn_sha256_b, hashlib.sha256) == True:
            print('valid')
            return True
        else:
            print('sigcheck2: invalid')
            return False
    except ecdsa.BadSignatureError:
        print('sigcheck2: Bad Signature')
        return False

#sample1
#sig='ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf8830b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b790'
#uncompressed pubkey
#pubkey='042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf'
#raw_txn='0100000001c8cc2b56525e734ff63a13bc6ad06a9e5664df8c67632253a8e36017aee3ee4000000000455141042f90074d7a5bf30c72cf3a8dfd1381bdbd30407010e878f3a11269d5f74a58788505cdca22ea6eab7cfb40dc0e07aba200424ab0d79122a653ad0c7ec9896bdf51aefeffffff0120f40e00000000001976a9141d30342095961d951d306845ef98ac08474b36a088aca727040001000000'

#sig_b=binascii.unhexlify(sig)
#pubkey_b=binascii.unhexlify(pubkey)
#raw_txn_b=binascii.unhexlify(raw_txn)

#check=sigcheck(sig_b, pubkey_b, raw_txn_b)
#print (check)


sig_b2='4bfa77725f598ccf358684d8fd2e752318554434e7cc4fd8563fba9d7e8048d0698d5872e3799da4d897289704cf23d3e4bff71a334104a2620676b0fc6378bc'
#sig_b2=binascii.unhexlify('304402204bfa77725f598ccf358684d8fd2e752318554434e7cc4fd8563fba9d7e8048d00220698d5872e3799da4d897289704cf23d3e4bff71a334104a2620676b0fc6378bc')
sig_b2=binascii.unhexlify(sig_b2)
pubkey_b2=binascii.unhexlify('026225155bd431cbdd7e6d8ab07e61cd30482158b66fa11fe3c2492cd0a9dd2310')
raw_tx_256_b=binascii.unhexlify('0a00903a1a547ea6c0cb20b1ef2e3926202f27c4dee9a656a57d8a6800ce67e3')
check2=sigcheck2(sig_b2, pubkey_b2, raw_tx_256_b)
print (check2)


sig_b3='5a86c1fd5a778f593d42ddb827ce06b0e75a2439dcfccfa1b6c729026473699043e120efa879937622f5dd0d72d4d6e9285be09f8433878303d79461cbd0d8f0'
sig_b3=binascii.unhexlify(sig_b3)
pubkey_b3=binascii.unhexlify('026225155bd431cbdd7e6d8ab07e61cd30482158b66fa11fe3c2492cd0a9dd2310')
#single hash256
raw_tx_256_b3=binascii.unhexlify('7770f5acb9675a95f9314b29b8cc157dc7145f7df5bcd8131065c30eafd366bb')
#double hash256
#raw_tx_256_b3=binascii.unhexlify('fb1c8d5bfab446673a96f34b8440b194df51765e9653fe3458646fc862eeaaca')
check3=sigcheck2(sig_b3, pubkey_b3, raw_tx_256_b3)
print (check3)



#sig_r_s=ParseSignature('3045022100ad0851c69dd756b45190b5a8e97cb4ac3c2b0fa2f2aae23aed6ca97ab33bf88302200b248593abc1259512793e7dea61036c601775ebb23640a0120b0dba2c34b79001')
#print (sig_r_s)
#sig_r_s=ParseSignature('304402206878b5690514437a2342405029426cc2b25b4a03fc396fef845d656cf62bad2c022018610a8d37e3384245176ab49ddbdbe8da4133f661bf5ea7ad4e3d2b912d856f01')
#print (sig_r_s)
#sig_r_s=ParseSignature('3045022100f739adc5b71bff4a168e82aab676fced416f758866313641d99a4a092b5b4cac02200e69bbc67470c4c817da06edd7509f3c841d2b5cd1cd267f5b1e8a1030cac00041')
#print (sig_r_s)
sig_r_s=ParseSignature('304402204bfa77725f598ccf358684d8fd2e752318554434e7cc4fd8563fba9d7e8048d00220698d5872e3799da4d897289704cf23d3e4bff71a334104a2620676b0fc6378bc')
print (sig_r_s)
