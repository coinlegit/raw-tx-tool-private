from segwit_addr import encode
from segwit_addr import decode
from hash_util   import hash160

hrp='tb' #testnet
#hrp='bc' #mainnet
pubkey='026ccfb8061f235cc110697c0bfb3afb99d82c886672f6b9b5393b25a434c0cbf3'
witver=0
script_pubkey_hash=hash160(pubkey.decode('hex')).encode('hex')
witprog=[int(x) for x in bytearray.fromhex(script_pubkey_hash)]
#print witprog
address=encode(hrp, witver, witprog)
print address
data=decode(hrp, address)
#print data


