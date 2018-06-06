#from bitcoin-core 1.60 the default address type is p2sh-segwit(P2SH-P2WPKH)
#validateの情報をgetaddressinfoに移動された

$ bash cli.bash  getnewaddress \"\" "p2sh-segwit"
2NEW4JdGwecPiaSMU84gMmmg7NwwNDADmZj

$ bash cli.bash  validateaddress 2NEW4JdGwecPiaSMU84gMmmg7NwwNDADmZj
{
  "isvalid": true,
  "address": "2NEW4JdGwecPiaSMU84gMmmg7NwwNDADmZj",
  "scriptPubKey": "a914e928cc1b9379ce4ce30f24b824c69a024924a1f787",
  "isscript": true,
  "iswitness": false
}

$ bash cli.bash  getaddressinfo 2NEW4JdGwecPiaSMU84gMmmg7NwwNDADmZj
{
  "address": "2NEW4JdGwecPiaSMU84gMmmg7NwwNDADmZj",
  "scriptPubKey": "a914e928cc1b9379ce4ce30f24b824c69a024924a1f787",
  "ismine": true,
  "iswatchonly": false,
  "isscript": true,
  "iswitness": false,
  "script": "witness_v0_keyhash",
  "hex": "0014c712299cbd34980b0d6b2dee8fe9a11fa816999e",
  "pubkey": "03302537fa9e3648ddbae25c068714c842b2540a1e9a5b3e38c628ba7471d33fa4",
  "embedded": {
    "isscript": false,
    "iswitness": true,
    "witness_version": 0,
    "witness_program": "c712299cbd34980b0d6b2dee8fe9a11fa816999e",
    "pubkey": "03302537fa9e3648ddbae25c068714c842b2540a1e9a5b3e38c628ba7471d33fa4",
    "address": "tb1qcufzn89axjvqkrtt9hhgl6dpr75pdxv7gkxmn8",
    "scriptPubKey": "0014c712299cbd34980b0d6b2dee8fe9a11fa816999e"
  },
  "label": "\"\"",
  "timestamp": 1528290018,
  "hdkeypath": "m/0'/0'/12'",
  "hdmasterkeyid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "labels": [
    {
      "name": "\"\"",
      "purpose": "receive"
    }
  ]
}

