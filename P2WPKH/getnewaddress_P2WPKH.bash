#get native P2WPKH segwit address(bech32 address)
#validateの情報をgetaddressinfoに移動された

$ bash cli.bash  getnewaddress \"\" "bech32"
tb1qx4h86l7v6pu3c8clkwm92el3u3qtrs7eygrayf

$ bash cli.bash  validateaddress tb1qx4h86l7v6pu3c8clkwm92el3u3qtrs7eygrayf
{
  "isvalid": true,
  "address": "tb1qx4h86l7v6pu3c8clkwm92el3u3qtrs7eygrayf",
  "scriptPubKey": "0014356e7d7fccd0791c1f1fb3b65567f1e440b1c3d9",
  "isscript": false,
  "iswitness": true,
  "witness_version": 0,
  "witness_program": "356e7d7fccd0791c1f1fb3b65567f1e440b1c3d9"
}

$ bash cli.bash  getaddressinfo tb1qx4h86l7v6pu3c8clkwm92el3u3qtrs7eygrayf
{
  "address": "tb1qx4h86l7v6pu3c8clkwm92el3u3qtrs7eygrayf",
  "scriptPubKey": "0014356e7d7fccd0791c1f1fb3b65567f1e440b1c3d9",
  "ismine": true,
  "iswatchonly": false,
  "isscript": false,
  "iswitness": true,
  "witness_version": 0,
  "witness_program": "356e7d7fccd0791c1f1fb3b65567f1e440b1c3d9",
  "pubkey": "02ae886896fcd31e60676272ffff98b6cbf5ad4b770db7247fe7bd244e212b071c",
  "label": "\"\"",
  "timestamp": 1528290007,
  "hdkeypath": "m/0'/0'/11'",
  "hdmasterkeyid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "labels": [
    {
      "name": "\"\"",
      "purpose": "receive"
    }
  ]
}

