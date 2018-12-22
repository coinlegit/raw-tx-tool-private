from hash_util import ripemd160,hash160,hash256,dhash256
from base58    import b58encode,b58encode_check,b58decode

#create p2sh address

#1 OP_ADD[0x93] 01 0x63 OP_EQUAL[0x87]
#OP_CHECKSIGVERIFY [0xad]
#OP_1              [0x51]
#OP_MUL            [0x95]
#0xAD OP_1 OP_1 OP_MUL

redeemScript='ad515195'

#2 Generate scriptPubKey as OP_HASH160 hash160(redeemScript) OP_EQUAL
data=hash160(redeemScript.decode('hex')).encode('hex')
print data
scriptPubKey='a914'+data+'87'

version='05' #mainnet
version='c4' #testnet
data=version+data

#print EncodeBase58Check(data.decode('hex'))
#3 Generate address with 0x05 prefix and double SHA256 hash checksum(=4bytes)
checksum=dhash256(data.decode('hex'))
checksum=checksum.encode('hex')[0:8]
addressHash=data+checksum

#4 bash58encode
address= b58encode(addressHash.decode('hex'))
print address

#2My2ApqGcoNXYceZC4d7fipBu4GodkbefHD

