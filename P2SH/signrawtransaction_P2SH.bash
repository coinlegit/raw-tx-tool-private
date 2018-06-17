# redeem pay to P2SH
#the bitcoin core not support sign this tx
#it show ["error": "Unable to sign input, invalid stack size (possibly missing key)"]

tx_id=94b231abe83d4b54d7179e122b5b712a2395bd24a14c4e5a31812ea22d127bd1
send_2_addr=mjRbyRrWh9MF6NWy9pij2XguvsrAv3EvnE
hex=$(bash cli.bash createrawtransaction "[{\"txid\":\"${tx_id}\",\"vout\":0}]" "{\"$send_2_addr\":1.2999}")

script_pub_key=`bash cli.bash getaddressinfo  2My2ApqGcoNXYceZC4d7fipBu4GodkbefHD | jq -r '.scriptPubKey'`
redeem_script=93016387

#hex=$(bash cli.bash signrawtransaction "$hex" "[{\"txid\":\"$tx_id\",\"vout\":0,\"scriptPubKey\":\"$script_pub_key\",\"redeemScript\":\"$redeem_script\"}]" "[\"${priv_key_1}\"]" | jq -r '.hex')
#hex=$(bash cli.bash signrawtransaction "$hex" "[{\"txid\":\"$tx_id\",\"vout\":0,\"scriptPubKey\":\"$script_pub_key\",\"redeemScript\":\"$redeem_script\"}]" | jq -r '.hex')
hex=$(bash cli.bash signrawtransaction "$hex" "[{\"txid\":\"$tx_id\",\"vout\":0,\"scriptPubKey\":\"$script_pub_key\"}]" | jq -r '.hex')
echo $hex

#curl -X POST -d "tx_hex=${hex}" https://chain.so/api/v2/send_tx/BTCTEST
#create txid=f6d4d14735ea283b0d3c8414c33283686ddcf0b01016616a4bf5aefcdbfc81f2

