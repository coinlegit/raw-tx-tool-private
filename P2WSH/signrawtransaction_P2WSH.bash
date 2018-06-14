# redeem pay to native segwit 2WSH
utxo_list=(
    #  $1:txid $2:vout $3:pub_key $4:redeem_script $5:amount $6:priv_key
    in=680d20d9ef5f2bd0cb09190a99dbefd9e1cb6e00054cc51588bc56a819b876e6:0:0020b05313905066ffd001e4b7694dbfe2b5baae212c2f2665c78584e68da30ce90a:522103d1531d7a373707e3057b53462f7b66e7ded258e39a1cda537bdbcb09b55b0ea02102ce0309065cdad727092440f13d6e2c1dabbc66fd6e4299e1642fdc65d2da303a52ae:1.2998:cW9fNAfjiAryUkpTyWQRaLWGFVahTyRoiTgH8G259DZig8kJU2VB
)
out_list=(
     outaddr=1.2997:n37g6n1JEsCGb9ctfoHT6epv8znnhtP522
)

key2_list=(
   #script public-key priv-key
   cQgY9UmyLWP5svEhCQYxKjnXDZct81BLjGgwKK3M16RaYNoHJV7p
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

#sign_cmd="${C_SIGN} "${raw_tx}" \"${sign_param_in}\" \"${sign_param_key}\" | jq  -r '.hex'"
sign_cmd="${C_SIGN} "${raw_tx}" \"${sign_param_in}\" \"${sign_param_key}\""
echo "sign1:" $sign_cmd
sign_out=`eval ${sign_cmd}`
raw_hex_tx=`echo "$sign_out" | jq -r '.hex'`
complete=`echo "$sign_out" | jq -r '.complete'`

if [ -z "$raw_hex_tx" ] ; then
    echo "sign1: Could not sign tx with ${sign_cmd}!"
    exit 1
fi

if [ "${complete}" = "false" ]; then
    sign_param_key="["
    for((i=0;i<${#key2_list[@]};i++))
    do
        if [ "$i" -gt 0 ]; then
         sign_param_key=${sign_param_key}","
        fi
        data="${key2_list[$i]}"
        key=$data
        key='\"'${key}'\"'
        sign_param_key=${sign_param_key}${key}

    done
    sign_param_key=${sign_param_key}"]"
    raw_tx="${raw_hex_tx}"
    sign_cmd2="${C_SIGN} "${raw_tx}" \"${sign_param_in}\" \"${sign_param_key}\""
    echo "sign2:" $sign_cmd2
    sign_out2=`eval ${sign_cmd2}`
    raw_hex_tx2=`echo "$sign_out2" | jq -r '.hex'`
    complete2=`echo "$sign_out2"   | jq -r '.complete'`

    if [ -z "$raw_hex_tx2" ] ; then
        echo " sign2: Could not sign tx with ${sign_cmd2}!"
        exit 1
    fi
fi
echo $raw_hex_tx2
#bash cli.bash decoderawtransaction "${raw_hex_tx2}"
#bash cli.bash sendrawtransaction "${raw_hex_tx}"


#OK
#https://live.blockcypher.com/btc-testnet/tx/0fa46045c7662d91fd522911de5e94f301e2983cc26af1b7cdb32dfbb1753aa8

