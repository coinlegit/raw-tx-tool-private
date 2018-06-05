cd /app/bitcoin/bin
   ./bitcoind \
       -datadir=/app/bitcoin/bin/data \
       -conf=/app/bitcoin/bin/bitcoin.conf \
       -testnet   \
       -maxconnections=0 \
       -daemon -keypool=1

