from hash_util import ripemd160,hash160,hash256,dhash256
from base58    import b58encode,b58encode_check,b58decode

#create p2pkh segwit address step by step
#compress pub key
#02d7c9e36a4d31039d4b94a43246a4a5f0767f2f55ef9a359901c82c41fb1e4bff

#1 Calculate the RIPEMD160 of the SHA256 of a public key
data='02d7c9e36a4d31039d4b94a43246a4a5f0767f2f55ef9a359901c82c41fb1e4bff'
data=hash160(data.decode('hex')).encode('hex')
#print data

#https://en.bitcoin.it/wiki/List_of_address_prefixes
#アドレスやスクリプトハッシュのバージョン情報(prefix)
#Pubkey hash (P2PKH address)
version='00' #mainnet
version='6F' #testnet
data=version+data

#print EncodeBase58Check(data.decode('hex'))
#2 Generate address with 0x05 prefix and double SHA256 hash checksum(=4bytes)
checksum=dhash256(data.decode('hex'))
checksum=checksum.encode('hex')[0:8]
addressHash=data+checksum

#5 bash58encode
address= b58encode(addressHash.decode('hex'))
print address

#2MsfZkQnEbsAYjTZa3PgB8SW7XRTdurVj8L

