from hash_util import ripemd160,hash160,hash256,dhash256
from base58    import b58encode,b58encode_check,b58decode

#1 Calculate the SHA256 of 2 of 3 public key
data1='2103d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea0'
data2='2102ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a'
data3=''
data='52'+data1+data2+data3+'52'+'ae'
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

