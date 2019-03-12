#https://github.com/libbitcoin/libbitcoin-system/wiki/Addresses-and-HD-Wallets
#https://github.com/libbitcoin/libbitcoin-system/wiki/Altcoin-Version-Mappings#bip44-altcoin-version-mapping-table
#https://github.com/libbitcoin/libbitcoin-system/wiki/Altcoin-Version-Mappings


#echo "radar blur cabbage chef fix engine embark joy scheme fiction master release" | bx mnemonic-to-seed |  bx hd-new -v 76066276
echo "radar blur cabbage chef fix engine embark joy scheme fiction master release" | bx mnemonic-to-seed |  bx hd-new -v 70615956

#echo -n 'xprv9s21ZrQH143K2weTjKTSMXUM1qmfYo2iDQGPrzsbirKyf9Qn325C8DtapD8dwUL2PU8ciZ9hYVSL4Q9VkygWBosS8FMuX65QqxZQmBDYSEq'  | \
#    bx hd-private --config bx.cfg -d -i 44 | \
#    bx hd-private -d -i 60 | \
#    bx hd-private -d -i 0  | \
#    bx hd-private -i 0     | \
#    bx hd-private -i 0     | \
#    bx hd-to-ec

echo -n 'xprv9s21ZrQH143K2weTjKTSMXUM1qmfYo2iDQGPrzsbirKyf9Qn325C8DtapD8dwUL2PU8ciZ9hYVSL4Q9VkygWBosS8FMuX65QqxZQmBDYSEq' | \
     bx hd-private --config bx.cfg -d -i 44 |   \
     bx hd-private -d -i 1  |   \
     bx hd-private -d -i 0  |   \
     bx hd-private -d -i 1  |   \
     bx hd-private    -i 32 |   \
     bx hd-to-ec

echo b96e9ccb774cc33213cbcb2c69d3cdae17b0fe4888a1ccd343cbd1a17fd98b18 | bx ec-to-public -u

