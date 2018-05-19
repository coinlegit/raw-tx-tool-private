# raw-tx-tool
some tips for create raw tx from script


1.redeem_pub_key_hash_input.py
<pre>
scriptPubKey: OP_DUP OP_HASH160 ＜pubKeyHash(20Byte)＞ OP_EQUALVERIFY OP_CHECKSIG
scriptSig: ＜sig＞ ＜pubKey(65Byte)＞
</pre>

<pre>
          prev_tx          tx
txin:                     scriptSig
txout:    scriptPubKey
</pre>

<pre>
script=scriptSig+scriptPubKey
      =＜sig＞ ＜pubKey(65Byte)＞ OP_DUP OP_HASH160 ＜pubKeyLen(1Byte)＞ ＜pubKeyHash(20Byte)＞ OP_EQUALVERIFY OP_CHECKSIG
the script run from empty stack and execute by order
</pre>

<pre>
 76       A9             14
 OP_DUP OP_HASH160    Bytes to push
 89 AB CD EF AB BA AB BA AB BA AB BA AB BA AB BA AB BA AB BA         88            AC
                       Data to push                            OP_EQUALVERIFY  OP_CHECKSIG
</pre>

2.redeem_public_key_input.py
<pre>
scriptPubKey: <pubKey> OP_CHECKSIG
scriptSig: <sig>
</pre>

3.redeem_segwit_input.py


4.segwit tx check example

[there is a btc testnet segwitoutput txid=56f87210814c8baef7068454e517a70da2f2103fc3ac7f687e32a228dc80e115](https://chain.so/tx/BTCTEST/56f87210814c8baef7068454e517a70da2f2103fc3ac7f687e32a228dc80e115)

 1. [native-P2WPKH:txid=d869f854e1f8788bcff294cc83b280942a8c728de71eb709a2c29d10bfe21b7c](https://chain.so/tx/BTCTEST/d869f854e1f8788bcff294cc83b280942a8c728de71eb709a2c29d10bfe21b7c)
 2. [native-P2WSH:txid=78457666f82c28aa37b74b506745a7c7684dc7842a52a457b09f09446721e11c](https://chain.so/tx/BTCTEST/78457666f82c28aa37b74b506745a7c7684dc7842a52a457b09f09446721e11c)
 3. [P2SH-WPKH:txid=8139979112e894a14f8370438a471d23984061ff83a9eba0bc7a34433327ec21](https://chain.so/tx/BTCTEST/8139979112e894a14f8370438a471d23984061ff83a9eba0bc7a34433327ec21)
 4. [P2SH-WSH:txid=954f43dbb30ad8024981c07d1f5eb6c9fd461e2cf1760dd1283f052af746fc88](https://chain.so/tx/BTCTEST/954f43dbb30ad8024981c07d1f5eb6c9fd461e2cf1760dd1283f052af746fc88)

## dependency
https://github.com/warner/python-ecdsa

## reference
https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki#specification
https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#witness-program
https://github.com/bitcoin/bips/blob/master/bip-0142.mediawiki#witness-program


