# raw-tx-tool
some tips for create raw tx from script

1.redeem_pub_key_hash_input.py

scriptPubKey: OP_DUP OP_HASH160 <pubKeyHash(20Byte)> OP_EQUALVERIFY OP_CHECKSIG
scriptSig: <sig> <pubKey(65Byte)>

<pre>
          prev_tx          tx
txin:                     scriptSig
txout:    scriptPubKey
</pre>

<pre>
script=scriptSig+scriptPubKey
      =<sig> <pubKey(65Byte)> OP_DUP OP_HASH160 <pubKeyLen(1Byte)> <pubKeyHash(20Byte)> OP_EQUALVERIFY OP_CHECKSIG
the script run from empty stack and execute by order
</pre>

<pre>
 76       A9             14
 OP_DUP OP_HASH160    Bytes to push
 89 AB CD EF AB BA AB BA AB BA AB BA AB BA AB BA AB BA AB BA         88            AC
                       Data to push                            OP_EQUALVERIFY  OP_CHECKSIG
</pre>

<pre>
2.redeem_public_key_input.py
scriptPubKey: <pubKey> OP_CHECKSIG
scriptSig: <sig>
</pre>

3.redeem_segwit_input.py

## dependency
https://github.com/warner/python-ecdsa


