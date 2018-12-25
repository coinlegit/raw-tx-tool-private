#create bare multisig address 2 of 2 [m of n]
#addr1=`bash cli.bash getnewaddress | grep 'bchtest:' | sed -e 's/bchtest:\(.*\)$/\1/'`
addr1=`bash cli.bash getnewaddress`
pubkey1=`bash cli.bash validateaddress "${addr1}" | jq -r '.pubkey'`

#addr2=`bash cli.bash getnewaddress | grep 'bchtest:' | sed -e 's/bchtest:\(.*\)$/\1/'`
addr2=`bash cli.bash getnewaddress`
pubkey2=`bash cli.bash validateaddress "${addr2}" | jq -r '.pubkey'`

echo ${pubkey1} ${pubkey2}
multi_addr=`bash cli.bash createmultisig 2 [\"${pubkey1}\",\"${pubkey2}\"]`
echo ${multi_addr} | jq '.'

