# redeem pay to P2SH-P2WPKH
utxo_list=(
    #  $1:txid $2:vout $3:pub_key $4:redeem_script $5:amount $6:priv_key
    in=b9c0b0bee666eb3b53ea501271c168da9a6a0527b66bfc87d8f1cbc5b1d7a2de:0:a914e928cc1b9379ce4ce30f24b824c69a024924a1f787:0014c712299cbd34980b0d6b2dee8fe9a11fa816999e:1.3:cTazeQXnngSWY4ocU5mMy9RRWR2TM2w1HkmnrxmSrnHoBGJFb1dT
)
out_list=(
     outaddr=1.2999:n37g6n1JEsCGb9ctfoHT6epv8znnhtP522
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
sep=','
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
    vout=${sep}'\"vout\":'${v_out}
    scriptPubKey=${sep}'\"scriptPubKey\":''\"'${script_pubkey}'\"'
    if [ ! -z "${redeem_script}"  ]; then
        redeemScript=${sep}'\"redeemScript\":''\"'${redeem_script}'\"'
    fi
    if [ ! -z "${amount}" ]; then
        amount=${sep}'\"amount\":'${amount}
    fi
    sign_param_in=${sign_param_in}${txid}${vout}${scriptPubKey}${redeemScript}${amount}
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

#echo ${sign_param_key}
if [[ ${sign_param_key} = '[\"\"]' ]]; then
    sign_param_key=
fi

#fee=0.0001
#send_amount=`echo "${redeem_amount}-${fee}" | bc`
#echo ${send_amount}

sign_cmd="${C_SIGN} "${raw_tx}" \"${sign_param_in}\" \"${sign_param_key}\" | jq  -r '.hex'"
echo $sign_cmd
raw_hex_tx=`eval ${sign_cmd}`
if [ -z "$raw_hex_tx" ] ; then
    echo " Could not sign tx with ${sign_cmd}!"
    exit 1
fi
echo $raw_hex_tx
bash cli.bash decoderawtransaction "${raw_hex_tx}"
#bash cli.bash sendrawtransaction "${raw_hex_tx}"


#OK
#https://live.blockcypher.com/btc-testnet/tx/175c6868e35b09e35722403e15a1afb7e48cbfe14b59c53caec1ece269a4f9cc/

