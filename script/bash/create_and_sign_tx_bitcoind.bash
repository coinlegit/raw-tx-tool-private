utxo_list=(
    #  $1:txid $2:vout $3:pub_key $4:redeem_script $5:amount $6:priv_key
    in=4ddd48ef8a22b2782dc83da2059b6349f711e4b713ba99c0aff758d49c10036e:1:5151865186518651865186518651865186518651865186518651865186518651865186518651865186518651865186518651865186518651865186518651865186::1.000000:
)
out_list=(
     outaddr=0.99:2MwCw5Vfw4qwfHCqp3pWXsGM3RnA1Njns5M
)

C_TX="./bitcoin-tx"
NET="-testnet"
C_SIGN="bash cli.bash signrawtransaction "
create_tx_cmd=" $C_TX $NET -create "
for i in "${utxo_list[@]}"
do
    data=$(echo $i | awk -F: {'print $1":"$2'})
    create_tx_cmd="${create_tx_cmd} $data"
done

for i in "${out_list[@]}"
do
    create_tx_cmd="${create_tx_cmd} $i"
done

#echo ${create_tx_cmd}
raw_tx=`eval ${create_tx_cmd}`
if [ -z "$raw_tx" ] ; then
    echo " Could not create tx with ${create_tx_cmd}!"
    exit 1
fi

sign_param_in="["
sep=","
for((i=0;i<${#utxo_list[@]};i++))
do
    if [ "$i" -gt 0 ]; then
        sign_param_in=${sign_param_in}","
    fi
    sign_param_in=${sign_param_in}"{"
    data="${utxo_list[$i]}"
    data=$(echo $data| sed -e s/^.*=//g)
    tx_id=$(echo $data| cut -d ":" -f 1)
    v_out=$(echo $data| cut -d ":" -f 2)
    script_pubkey="$(echo $data| cut -d ":" -f 3)"
    redeem_script="$(echo $data| cut -d ":" -f 4)"
    amount="$(echo $data| cut -d ":" -f 5)"

    txid='\"txid\":''\"'${tx_id}'\"'
    vout='\"vout\":'${v_out}
    scriptPubKey='\"scriptPubKey\":''\"'${script_pubkey}'\"'
    redeemScript='\"redeemScript\":''\"'${redeem_script}'\"'
    amount='\"amount\":'${amount}
    sign_param_in=${sign_param_in}${txid}${sep}${vout}${sep}${scriptPubKey}${sep}${redeemScript}${sep}${amount}
    sign_param_in=${sign_param_in}"}"
done
sign_param_in=${sign_param_in}"]"
#echo ${sign_param_in}

sign_param_key="["

for((i=0;i<${#utxo_list[@]};i++))
do
    if [ "$i" -gt 0 ]; then
        sign_param_key=${sign_param_key}","
    fi
    data="${utxo_list[$i]}"
    data=$(echo $data| sed -e s/^.*=//g)
    key=$(echo $data| cut -d ":" -f 6)
    key='\"'${key}'\"'
    sign_param_key=${sign_param_key}${key}
done
sign_param_key=${sign_param_key}"]"

echo ${sign_param_key}
if [[ ${sign_param_key} = '[\"\"]' ]]; then
    sign_param_key=
fi

#fee=0.0001
#send_amount=`echo "${redeem_amount}-${fee}" | bc`
#echo ${send_amount}

sign_cmd="${C_SIGN} "${raw_tx}" \"${sign_param_in}\" \"${sign_param_key}\" | jq  -r '.hex'"
raw_hex_tx=`eval ${sign_cmd}`
if [ -z "$raw_hex_tx" ] ; then
    echo " Could not sign tx with ${sign_cmd}!"
    exit 1
fi
echo $raw_hex_tx
#bash cli.bash decoderawtransaction "${raw_hex_tx}" 
#bash cli.bash sendrawtransaction "${raw_hex_tx}" 


#OK:7f231b99b4cad819cfda0d91301ac1219d033e2ae7681afeaa21f31b9e416a9e
#OK128b5f43928a954b08f6c58a3f8e02e2b30dabf07364853fcfe0a506cf81f47c
