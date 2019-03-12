#Info: Create a mnemonic seed (BIP39) from entropy. WARNING: mnemonic
#should be created from properly generated entropy.
#bx mnemonic-new aadf00dbaadf00dbaadf00dbaadf00d
#16bytes entropy
mnemonic=$(bx seed -b 128 | bx mnemonic-new --language en)  #12
echo ${mnemonic}
#mnemonic='pause barrel shock rebuild harbor oven auction theory turtle cousin hat pride'
master_seed=$(bx mnemonic-to-seed --language en ${mnemonic})
echo ${master_seed}
echo ${master_seed} | bx hd-new -v 76066276 
#64bytes/512bits
#echo -n ${master_seed} | wc -c




