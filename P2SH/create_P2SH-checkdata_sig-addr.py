from hash_util import ripemd160,hash160,hash256,dhash256
from base58    import b58encode,b58encode_check,b58decode

#create p2sh address

#1 create p2sh checkdata-sig address from below data text
#signature
sig_r='0220'+"2caa3f50ec00dcf2eff56bb9e14d4af2b54f0f7ecbdee576c8e5f128a50382b4"
sig_s='0220'+"6eaa0117977269a2ba9eb5698861141681a81479e5f32e8f9bcebacc07062616"
sig_l=len(sig_r)/2+len(sig_s)/2
sig='30'+hex(sig_l)[2:]+sig_r+sig_s
le=hex(len(sig)/2)
print "sig=",sig

#redeem script
msg="0064d431be56e62f41e05a4af9dd662d4364878cce9e794ecbfcf56c311eabb68f"  #hash256('I like you yuka')

compress_public_key="02827083a0162c03a27f5c23f9376404d60b818d09f841b20d32c9826ca6d9817e"
check_data_sig_opcode='ba'
#redeemScript='1f48656c6c6f20776f726c64210a04001308000605025e0c518004ff0000000c2102a788d320086c086c71e15d34e62a2308240afccc2325bb34f07edf56706f62a6ba'
#print hex(len(msg)/2)[2:]
msg_l=hex(len(msg)/2)[2:]
#msg_l=msg_l.rjust(4, '0')
msg=msg_l+msg
pub_key_l=hex(len(compress_public_key)/2)[2:]
compress_public_key=pub_key_l+compress_public_key
redeemScript=msg+compress_public_key+check_data_sig_opcode
#len
#redeemScript_l=str(hex(len(redeemScript)/2)).strip('0x')
#redeemScript=redeemScript_l+redeemScript
print "redeemScript=",redeemScript


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

