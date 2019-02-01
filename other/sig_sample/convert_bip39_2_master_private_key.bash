#root seed to master private key
#mnemonic to root seed 64 bytes
#converting the BIP 39 mnemonic to a seed
root_seed=$(echo "system guard object voyage slot hint embody faint embrace fresh tide diary" | bx mnemonic-to-seed -p "")

#master_priv_chain_code=$( echo ${root_seed} | bx base16-decode | hmac --algorithm sha512 --key "Bitcoin seed" -  )
#master_priv_chain_code=$( echo ${root_seed} | bx base16-decode | openssl dgst -sha512 -hmac "secret_key" | awk '{print $2}' )
master_priv_chain_code=$( echo ${root_seed} | bx base16-decode | openssl dgst -sha512 -hmac "Bitcoin seed" | awk '{print $2}' )

master_private_key=$(echo ${master_priv_chain_code} | cut -c 1-64)
chain_code=$(echo ${master_priv_chain_code} | cut -c 65-128)
master_public_key=$(echo ${master_private_key} | bx ec-to-public)

echo "master_private_key:${master_private_key}"
echo "chain_code        :${chain_code}"
echo "master_public_key :${master_public_key}"

