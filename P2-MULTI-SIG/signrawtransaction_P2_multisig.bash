# redeem pay to P2SH-multisig
#create P2 script multisig address

addr1=$(bash cli.bash getnewaddress)
addr2=$(bash cli.bash getnewaddress)
pub_key1=$(bash cli.bash getaddressinfo $addr1 | jq -r '.pubkey')
pub_key2=$(bash cli.bash getaddressinfo $addr2 | jq -r '.pubkey')
bash cli.bash createmultisig 2 "[\"$pub_key1\",\"$pub_key2\"]"


addr1=$(bash cli.bash getnewaddress)
addr2=$(bash cli.bash getnewaddress)
pub_key1=$(bash cli.bash getaddressinfo $addr1 | jq -r '.pubkey')
pub_key2=$(bash cli.bash getaddressinfo $addr2 | jq -r '.pubkey')
bash cli.bash createmultisig 1 "[\"$pub_key1\"]"

bash cli.bash createmultisig 1 "[\"$pub_key1\",\"$pub_key2\"]"

#send to 2MsggmDQxBZFeJaByQqhHJkGAzmSbfHKJUZ
#94b231abe83d4b54d7179e122b5b712a2395bd24a14c4e5a31812ea22d127bd1

#redeem 2MsggmDQxBZFeJaByQqhHJkGAzmSbfHKJUZ

tx_id=94b231abe83d4b54d7179e122b5b712a2395bd24a14c4e5a31812ea22d127bd1
send_2_addr=mjRbyRrWh9MF6NWy9pij2XguvsrAv3EvnE
hex=$(bash cli.bash createrawtransaction "[{\"txid\":\"${tx_id}\",\"vout\":0}]" "{\"$send_2_addr\":1.2999}")

script_pub_key=`bash cli.bash getaddressinfo 2MsggmDQxBZFeJaByQqhHJkGAzmSbfHKJUZ | jq -r '.scriptPubKey'`
redeem_script=522102c274584679c85d9b00d2e03b0762714e057d9c078aa4084a31c8d116732fda7b2103c5a4e0a17e5b2b769253e0fb909bad8cdc5e9b59a8b701cb4c528974feaa158452ae
priv_key_1=cRHfHM81qBDf4FesJBBGT5ATphn57RkPyKPeMmCw8Y2KWr3WQmaw
priv_key_2=cVgTA4wPupoGU8zD29sFNZB8MfYv62LY2h5gsaoMgLWQz6zRgGEE

hex=$(bash cli.bash signrawtransaction "$hex" "[{\"txid\":\"$tx_id\",\"vout\":0,\"scriptPubKey\":\"$script_pub_key\",\"redeemScript\":\"$redeem_script\"}]" "[\"${priv_key_1}\"]" | jq -r '.hex')
echo $hex
hex=$(bash cli.bash signrawtransaction $hex "[{\"txid\":\"$tx_id\",\"vout\":0,\"scriptPubKey\":\"$script_pub_key\",\"redeemScript\":\"$redeem_script\"}]" "[\"${priv_key_2}\"]" | jq -r '.hex')


curl -X POST -d "tx_hex=${hex}" https://chain.so/api/v2/send_tx/BTCTEST

#create txid=f6d4d14735ea283b0d3c8414c33283686ddcf0b01016616a4bf5aefcdbfc81f2

script=00483045022100877657833e8119f8f519f1ef9655473aa925877b0ec6d78d5cdcb74552207b81022019f083a85e04fe1ebe3869d3555e740b577b3341db6cc9d028fc0f55e52fb77d0147304402206aa485d12dad80de7454bd6795cfe756aca82e81f36c2eba50269f7e4b6d3efa02205e250b703daa6d8ee373a474cc8dbc3be37b6a80d28a99d062ad6cbffd3b83090147522102c274584679c85d9b00d2e03b0762714e057d9c078aa4084a31c8d116732fda7b2103c5a4e0a17e5b2b769253e0fb909bad8cdc5e9b59a8b701cb4c528974feaa158452ae

 "asm":
    "0 3045022100877657833e8119f8f519f1ef9655473aa925877b0ec6d78d5cdcb74552207b81022019f083a85e04fe1ebe3869d3555e740b577b3341db6cc9d028fc0f55e52fb77d01  #sig1
       304402206aa485d12dad80de7454bd6795cfe756aca82e81f36c2eba50269f7e4b6d3efa02205e250b703daa6d8ee373a474cc8dbc3be37b6a80d28a99d062ad6cbffd3b830901    #sig2
       522102c274584679c85d9b00d2e03b0762714e057d9c078aa4084a31c8d116732fda7b2103c5a4e0a17e5b2b769253e0fb909bad8cdc5e9b59a8b701cb4c528974feaa158452ae",  #redeem_script

