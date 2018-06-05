cd /app/bitcoin/bin
   ./bitcoin-cli \
        -datadir=/app/bitcoin/bin/data \
        -testnet \
        -conf=/app/bitcoin/bin/bitcoin.conf \
       $@

