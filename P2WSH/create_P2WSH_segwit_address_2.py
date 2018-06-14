from segwit_addr import encode
from segwit_addr import decode
from hash_util   import hash160,hash256

hrp='tb' #testnet
#hrp='bc' #mainnet

pubkey1='2103d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea0'
pubkey2='2102ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a'
pubkey3=''
data='52'+pubkey1+pubkey2+pubkey3+'52'+'ae'
script_hash=hash256(data.decode('hex')).encode('hex')

witver=0
witprog=[int(x) for x in bytearray.fromhex(script_hash)]
#print witprog
address=encode(hrp, witver, witprog)
print address
data=decode(hrp, address)
#print data


