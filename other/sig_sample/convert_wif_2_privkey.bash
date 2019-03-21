wif='5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreCw2uZTA'
#bx wif-to-ec L21LJEeJwK35wby1BeTjwWssrhrgQE2MZrpTm2zbMC677czAHHu3
#ec=$(bx wif-to-ec $wif)
#echo $ec
#echo $ec | bx ec-to-public | bx ec-to-address

privkey=$(bx seed | bx ec-new)
address=$(echo ${privkey}| bx ec-to-public | bx ec-to-address)
utxo=$(curl -s https://blockstream.info/api/address/${address}/utxo | jq .)
#echo ${privkey} ${address}
if [ "${utxo}" != "[]" ] ; then
    echo ${privkey} ${address} ${utxo}
fi

#bx ec-new
#entropy[seed] to priv 
#echo "a76e98bda0269269a3a2bbc98108ac6cc614c54b94d48f502745b5e74eaff613" | bx ec-new
#echo "a76e98bda0269269a3a2bbc98108ac6cc614c54b94d48f502745b5e74eaff613" | bx ec-new | bx ec-to-public | bx ec-to-address



