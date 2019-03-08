#Info: Create a mnemonic seed (BIP39) from entropy. WARNING: mnemonic
#should be created from properly generated entropy.
#bx mnemonic-new aadf00dbaadf00dbaadf00dbaadf00d
#16bytes entropy
bx seed -b 128 | bx mnemonic-new --language es
bx seed -b 1024 | bx mnemonic-new --language ja
bx seed -b 192 | bx mnemonic-new --language ja



