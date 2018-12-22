# bch-hard-fork


* Canonical Transaction Order
* new opcodes

1.  OP_CHECKDATASIG
2.  OP_CHECKDATASIGVERIFY

<pre>
OP_CHECKDATASIG
<sig> <msg> <pubKey> OP_CHECKDATASIG
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#p2sh address
```
msg="0064d431be56e62f41e05a4af9dd662d4364878cce9e794ecbfcf56c311eabb68f"  #hash256('I like you yuka')
compress_public_key="02827083a0162c03a27f5c23f9376404d60b818d09f841b20d32c9826ca6d9817e"
check_data_sig_opcode='ba'
msg_l=hex(len(msg)/2)[2:]
msg=msg_l+msg
pub_key_l=hex(len(compress_public_key)/2)[2:]
compress_public_key=pub_key_l+compress_public_key
redeemScript=msg+compress_public_key+check_data_sig_opcode
hash160(redeemScript.decode('hex')).encode('hex') -->p2sh address
```

#signature
sign(msg)--> #0221 00ad28f912f1240f59c646529d5b8e9a4d5185396478bfe4abdf5e7a87706879cb
             #0220 46f649e1d3d09a30278d15e22f0f23a684b7ac1acaa75176eeb63733e7dc8aaa

I also created a test tx to confirm the OP_CHECKDATASIG,
the tx is [0450eaef8e972ae7b24960785cbd8b665c45e4a109ef4b6ee580c652ad814a3b](https://www.blocktrail.com/tBCC/tx/0450eaef8e972ae7b24960785cbd8b665c45e4a109ef4b6ee580c652ad814a3b?txoutIdx=1)
the tx is pay to 2MxVZaGsFJzNJhkkDh51oZhTpoJH6sq8FyU, and spent tx is 
[4dc9b682c9baf17f2d7b61dece01eb88677efaacce21833ad0688c6f74e52b5b](https://www.blocktrail.com/tBCC/tx/4dc9b682c9baf17f2d7b61dece01eb88677efaacce21833ad0688c6f74e52b5b?txinIdx=0)

(*)warning this p2sh is anyone can spend when release it's scriptSig

OP_CHECKDATASIGVERIFY
```
OP_IF 
    <sig_CDSV> <msg> <pubkey_CDSV> OP_CHECKDATASIGVERIFY <pubkeyBCH>
OP_ELSE
    <pubkeyBSV>
OP_ENDIF
OP_CHECKSIG

<SigBSV> OP_TRUE
the sample tx is [23acdda462064b0f6dae54118d11a15001af35243752b273af2f3815de97f77f](https://www.blocktrail.com/tBCC/tx/23acdda462064b0f6dae54118d11a15001af35243752b273af2f3815de97f77f?txinIdx=0)
the spent tx is  [85f04c9a26d07e83744cef5b4b1b0b7158f3bdf401d7774f12f79862729c47c0](https://www.blocktrail.com/tBCC/tx/85f04c9a26d07e83744cef5b4b1b0b7158f3bdf401d7774f12f79862729c47c0?txinIdx=0) 

(*) this p2sh use to split bitcoin-bch and bitcoin-sv coin split
```

</pre>

