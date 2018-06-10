from base58 import b58decode
def wif_2_privkey(wif):
     decoded=b58decode(wif)
     print decoded.encode('hex')
     key_hash=decoded[0:-4]
     check_sum=decoded[-4:]
     if len(key_hash) == 34:
         return key_hash[1:-1].encode('hex')
     if len(key_hash) == 33:
         return key_hash[1:].encode('hex')

def main():
    d=wif_2_privkey('cQuzMWdzbJezujAaAiMNq4Gr6zcFZt7BeD2VGUEN3LYBzZYgipRF')
    print d

if __name__ == '__main__':
    main()

