#get P2PKH segwit address(legacy address)
#validateの情報をgetaddressinfoに移動された

$ bash cli.bash  getnewaddress \"\" "legacy"
n37g6n1JEsCGb9ctfoHT6epv8znnhtP522

$ bash cli.bash  validateaddress n37g6n1JEsCGb9ctfoHT6epv8znnhtP522
{
  "isvalid": true,
  "address": "n37g6n1JEsCGb9ctfoHT6epv8znnhtP522",
  "scriptPubKey": "76a914ecebae831bbfbd7827542a82da4dc136e1288f7188ac",
  "isscript": false,
  "iswitness": false
}

$ bash cli.bash  getaddressinfo n37g6n1JEsCGb9ctfoHT6epv8znnhtP522
{
  "address": "n37g6n1JEsCGb9ctfoHT6epv8znnhtP522",
  "scriptPubKey": "76a914ecebae831bbfbd7827542a82da4dc136e1288f7188ac",
  "ismine": true,
  "iswatchonly": false,
  "isscript": false,
  "iswitness": false,
  "pubkey": "02d7c9e36a4d31039d4b94a43246a4a5f0767f2f55ef9a359901c82c41fb1e4bff",
  "iscompressed": true,
  "label": "\"\"",
  "timestamp": 1528292025,
  "hdkeypath": "m/0'/0'/21'",
  "hdseedid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "hdmasterkeyid": "94a45e17cb46272e4d39e06ec00fc38c729b160a",
  "labels": [
    {
      "name": "\"\"",
      "purpose": "receive"
    }
  ]
}

