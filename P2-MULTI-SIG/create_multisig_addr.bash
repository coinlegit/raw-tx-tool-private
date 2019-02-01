# redeem pay to P2SH-multisig
#create P2 script multisig address

addr1=$(bash cli.bash getnewaddress)
addr2=$(bash cli.bash getnewaddress)
pub_key1=$(bash cli.bash getaddressinfo $addr1 | jq -r '.pubkey')
pub_key2=$(bash cli.bash getaddressinfo $addr2 | jq -r '.pubkey')
bash cli.bash createmultisig 2 "[\"$pub_key1\",\"$pub_key2\"]"

