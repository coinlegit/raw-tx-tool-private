from hash_util import ripemd160,hash160,hash256,dhash256
from base58    import b58encode,b58encode_check,b58decode

#create p2sh-p2wpkh segwit address step by step
#hash160=ripemd160(hash256(input))
#Public key - compressed:
#03fac6879502c4c939cfaadc45999c7ed7366203ad523ab83ad5502c71621a85bb

#wif priv key
##L5mHKZsCLS27nSoGM3RdAwuxjvg7XhJdP25LgqdXe6zF11wpWdbT
#compress pub key
#03fac6879502c4c939cfaadc45999c7ed7366203ad523ab83ad5502c71621a85bb

#1 Calculate the RIPEMD160 of the SHA256 of a public key
data='03fac6879502c4c939cfaadc45999c7ed7366203ad523ab83ad5502c71621a85bb'
data=hash160(data.decode('hex')).encode('hex')
#print data
#2 Create P2SH redeemScript as OP_PUSH publicKeyHash
redeemScript='0014'+data

#3 Generate scriptPubKey as OP_HASH160 hash160(redeemScript) OP_EQUAL
data=hash160(redeemScript.decode('hex')).encode('hex')
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

