## summary

<pre>
when sign tx use bitcoin-abc daemon with incorrect redeem_amount,
the bitcoin-cli show 「16: mandatory-script-verify-flag-failed (Signature must be zero for failed CHECK(MULTI)SIG operation)」,
means signature is wrong, because bitcoin-abc signrawtransaction need correc amount field.
you can produce from below code.
</pre>

```
redeem_amount=5.4999
redeem_tx_id=3ee6fbfb0b4a3d075b023c0f169fcdc0692fcb9f41f33fa77cc44bac17102c49
send_addr=2MwCw5Vfw4qwfHCqp3pWXsGM3RnA1Njns5M
fee=0.0001
send_amount=`echo "${redeem_amount}-${fee}" | bc`
#echo ${send_amount}
script_pubkey=76a914b01633747cbc4921912adb98b28cebfbc77662c188ac
private_key=cRYcUiBDPZKpJR268k8PpiMews7Fv84w3sf3t1NsWMJuKDSnUBJu

raw_tx=$(bash cli.bash createrawtransaction  "[{\"txid\":\"${redeem_tx_id}\",\"vout\":0}]" "{\"${send_addr}\":${send_amount}}")
raw_hex_tx=$(bash cli.bash signrawtransaction "${raw_tx}" "[{\"txid\":\"${redeem_tx_id}\",\"vout\":0,\"scriptPubKey\":\"${script_pubkey}\",\"redeemScript\":\"\",\"amount\":${redeem_amount}}]" "[\"${private_key}\"]" | jq  -r '.hex')
echo "${raw_hex_tx}"
bash cli.bash sendrawtransaction "${raw_hex_tx}"

```
