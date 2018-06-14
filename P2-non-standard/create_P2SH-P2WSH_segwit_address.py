from hash_util import ripemd160,hash160,hash256,dhash256
from base58    import b58encode,b58encode_check,b58decode

#1 Calculate the SHA256 of 2 of 3 public key
data1='21026ccfb8061f235cc110697c0bfb3afb99d82c886672f6b9b5393b25a434c0cbf3'
data2='2103befa190c0c22e2f53720b1be9476dcf11917da4665c44c9c71c3a2d28a933c35'
data3='2102be46dc245f58085743b1cc37c82f0d63a960efa43b5336534275fc469b49f4ac'
data='52'+data1+data2+data3+'53'+'ae'
data='020203040569696969'
data=hash256(data.decode('hex')).encode('hex')
#print data
#2 Create P2SH redeemScript as OP_PUSH publicKeyHash
redeemScript='0020'+data

#3 Generate scriptPubKey as OP_HASH160 hash160(redeemScript) OP_EQUAL
data=hash160(redeemScript.decode('hex')).encode('hex')
print data
scriptPubKey='a914'+data+'87'

version='05' #mainnet
version='c4' #testnet
data=version+data

#print EncodeBase58Check(data.decode('hex'))
#4 Generate address with 0x05 prefix and double SHA256 hash checksum(=4bytes)
checksum=dhash256(data.decode('hex'))
checksum=checksum.encode('hex')[0:8]
addressHash=data+checksum

#5 bash58encode
address= b58encode(addressHash.decode('hex'))
print address

#33voQqbNAYyig272KjcX8GkucWn2x25WEg

