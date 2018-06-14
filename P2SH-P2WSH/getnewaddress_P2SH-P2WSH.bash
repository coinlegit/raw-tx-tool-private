#from bitcoin-core 1.60 the createmultisig support address type is p2sh-segwit(P2SH-P2WSH)
#https://github.com/bitcoin/bitcoin/pull/13072/commits/fd130fa73766dc17e4f9bfb39d2625273efefecf
#それ以前にaddwitnessaddressで生成する
#validateの情報をgetaddressinfoに移動された

$ bash cli.bash  getnewaddress \"\" "p2sh-segwit"
2N21FSQTH8Xhm9XDLMze6vTumBcCuqYtMy6
$ bash cli.bash  getnewaddress \"\" "p2sh-segwit"
2N8wy2Qo8P21H4911DJxcbDyECHwkWWEZWL

#create 2 of 2 multisig
$ pubkey1=$(bash cli.bash getaddressinfo 2N21FSQTH8Xhm9XDLMze6vTumBcCuqYtMy6 | jq -r '.pubkey')
$ pubkey2=$(bash cli.bash getaddressinfo 2N8wy2Qo8P21H4911DJxcbDyECHwkWWEZWL | jq -r '.pubkey')
echo $pubkey1
echo $pubkey2
#$ bash createmultisig 2 "[\"$pubkey1\",\"$pubkey2\"]" "p2sh-segwit"
$ bash createmultisig 2 "[\"$pubkey1\",\"$pubkey2\"]" 
{
  "address": "2NFR7TWTLqJnQ5pC2L4q2P5SmqqTXxxJHef",
  "redeemScript": "522103d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea02102ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a52ae"
}
$ bash cli.bash  getaddressinfo 2NFR7TWTLqJnQ5pC2L4q2P5SmqqTXxxJHef
{
  "address": "2NFR7TWTLqJnQ5pC2L4q2P5SmqqTXxxJHef",
  "scriptPubKey": "a914f33179b2b9bb0186c2cfb88d42d38c899234a83587",
  "ismine": false,
  "iswatchonly": false,
  "isscript": true,
  "iswitness": false,
  "labels": [
  ]
}

$ bash cli.bash  decodescript 522103d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea02102ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a52ae
{
  "asm": "2 03d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea0 02ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a 2 OP_CHECKMULTISIG",
  "reqSigs": 2,
  "type": "multisig",
  "addresses": [
    "mk7DXALUwXww2oGmdKRQ4wv6BW6BpmwjQo",
    "n4JGtdbBs84pZg1Xk6LXkg6eJQcMgDecXv"
  ],
  "p2sh": "2NFR7TWTLqJnQ5pC2L4q2P5SmqqTXxxJHef",
  "segwit": {
    "asm": "0 b05313905066ffd001e4b7694dbfe2b5baae212c2f2665c78584e68da30ce90a",
    "hex": "0020b05313905066ffd001e4b7694dbfe2b5baae212c2f2665c78584e68da30ce90a",
    "reqSigs": 1,
    "type": "witness_v0_scripthash",
    "addresses": [
      "tb1qkpf38yzsvmlaqq0yka55m0lzkka2ugfv9unxt3u9snngmgcvay9q9yzcn6"
    ],
    "p2sh-segwit": "2NDEP4aVZCwQffz8CrGtxrdfa7sMdhrdBur"
  }
}

$ bash cli.bash  getaddressinfo mk7DXALUwXww2oGmdKRQ4wv6BW6BpmwjQo
{
  "address": "mk7DXALUwXww2oGmdKRQ4wv6BW6BpmwjQo",
  "scriptPubKey": "76a914325b5b197541dbff97a757f4e5bafd489e511ea588ac",
  "ismine": true,
  "iswatchonly": false,
  "isscript": false,
  "iswitness": false,
  "pubkey": "03d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea0",
  "iscompressed": true,
  "timestamp": 1528291576,
  "hdkeypath": "m/0'/0'/18'",
  "hdseedid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "hdmasterkeyid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "labels": [
  ]
}

$ bash cli.bash  getaddressinfo n4JGtdbBs84pZg1Xk6LXkg6eJQcMgDecXv
{
  "address": "n4JGtdbBs84pZg1Xk6LXkg6eJQcMgDecXv",
  "scriptPubKey": "76a914f9e5024220e7a82c754631fb770826a984f3962d88ac",
  "ismine": true,
  "iswatchonly": false,
  "isscript": false,
  "iswitness": false,
  "pubkey": "02ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a",
  "iscompressed": true,
  "timestamp": 1528291584,
  "hdkeypath": "m/0'/0'/19'",
  "hdseedid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "hdmasterkeyid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "labels": [
  ]
}


$ bash cli.bash  getaddressinfo 2NDEP4aVZCwQffz8CrGtxrdfa7sMdhrdBur
{
  "address": "2NDEP4aVZCwQffz8CrGtxrdfa7sMdhrdBur",
  "scriptPubKey": "a914db39aca19a88cb8a521baad652dbfeed7ce66f0387", //pay to p2sh-p2wsh scriptPubKey=hash160( 0020+hash256(redeemScript) )
  "ismine": false,
  "iswatchonly": false,
  "isscript": true,
  "iswitness": false,
  "labels": [
  ]
}

$ bash cli.bash  decodescript 522103d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea02102ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a52ae |  jq -r '.segwit."p2sh-segwit"'

