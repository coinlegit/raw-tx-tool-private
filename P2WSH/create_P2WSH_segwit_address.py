from segwit_addr import encode
from segwit_addr import decode
from hash_util   import hash160,hash256

hrp='tb' #testnet
#hrp='bc' #mainnet

pubkey1='21026ccfb8061f235cc110697c0bfb3afb99d82c886672f6b9b5393b25a434c0cbf3'
pubkey2='2103befa190c0c22e2f53720b1be9476dcf11917da4665c44c9c71c3a2d28a933c35'
pubkey3='2102be46dc245f58085743b1cc37c82f0d63a960efa43b5336534275fc469b49f4ac'
data='52'+pubkey1+pubkey2+pubkey3+'53'+'ae'
script_hash=hash256(data.decode('hex')).encode('hex')

witver=0
witprog=[int(x) for x in bytearray.fromhex(script_hash)]
#print witprog
address=encode(hrp, witver, witprog)
print address
data=decode(hrp, address)
#print data


