# raw-tx-tool
<pre>
some tips for create raw tx from script
bitcoinのトランザクションを理解するため幾つかのTXの基本の内容を紹介する。
詳細のTXの署名の過程と方法をpythonスクリプトで実装する。
</pre>
1.bitcoinの基本スクリプト
<pre>

OP_CODE             HEX
------------------------
OP_DUP              76
OP_HASH160          a9
OP_EQUALVERIFY      88
OP_CHECKSIG         ac
OP_EQUAL            87

[1]P2PKH #################################
scriptSig:    ＜signature＞ ＜pubkey＞
scriptPubKey: 76 a9 14 ＜20-byte-key-hash＞ 88 CHECKSIG

check-sig-operation
1)hash160(scriptSig.＜pubkey＞)=scriptPubKey.＜20-byte-pubkey-hash＞
2)＜scriptSig＞ ＜scriptPubKey＞

[2]P2SH-P2WPKH##############################
witness:     ＜signature＞ ＜pubkey＞
scriptSig:   ＜0 ＜20-byte-pubkey-hash＞＞
             (0x160014{20-byte-pubkey-hash})
scriptPubKey: HASH_160 ＜20-byte-script-hash＞ EQUAL

check-sig-operation
1)hash160(scriptSig)=scriptPubKey.＜20-byte-script-hash＞
2)witness.size=2
3)＜signature＞ ＜pubkey＞ CHECKSIG

[3]P2WPKH #################################
P2WSH nested in BIP16 P2SH

witness:      ＜signature＞ ＜pubkey＞
scriptSig:    (empty)
scriptPubKey: 00 ＜20-byte-pubkey-hash＞
              (0x0014{20-byte-pubkey-hash})
                     {20byte = P2WPKH witness program}

check-sig-operation
1)hash160(witness.＜pubkey＞)=＜20-byte-pubkey-hash＞
2)witness.size=2
3)＜signature＞ ＜pubkey＞ CHECKSIG


[4]P2SH-P2WSH##############################
witness:     0 ＜signature1＞ ＜1 ＜pubkey1＞ ＜pubkey2＞ 2 CHECKMULTISIG＞
scriptSig:  ＜0 ＜32-byte-hash＞＞
            (0x220020{32-byte-hash})
scriptPubKey: HASH160 ＜20-byte-hash＞ EQUAL
             (HASH_160 14{20-byte-hash} EQUAL)

check-sig-operation
1)hash160(scriptSig)=scriptPubKey.＜20-byte-hash＞
2)0 ＜signature1＞ 1 ＜pubkey1＞ ＜pubkey2＞ 2 CHECKMULTISIG

[5]P2WSH##############################
witness:     0 ＜signature1＞ ＜1 ＜pubkey1＞ ＜pubkey2＞ 2 CHECKMULTISIG＞
scriptSig:  (empty) 
scriptPubKey: 0 ＜32-byte-hash＞
             (0x0020{32-byte-hash})

check-sig-operation
1)sha256(witness.＜1 ＜pubkey1＞ ＜pubkey2＞ 2 CHECKMULTISIG＞)=scriptPubKey.＜32-byte-hash＞
2)0 ＜signature1＞ 1 ＜pubkey1＞ ＜pubkey2＞ 2 CHECKMULTISIG

</pre>

2.segwit tx check example

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

