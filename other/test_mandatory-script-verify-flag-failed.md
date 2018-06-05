## summary

<pre>
when sign tx use bitcoin-abc daemon with incorrect redeem_amount,
the bitcoin-cli show 「16: mandatory-script-verify-flag-failed (Signature must be zero for failed CHECK(MULTI)SIG operation)」,
means signature is wrong, because bitcoin-abc signrawtransaction need correct amount field.
you can produce from below code.
</pre>

```
redeem_amount=5.4999
redeem_tx_id=3ee6fbfb0b4a3d075b023c0f169fcdc0692fcb9f41f33fa77cc44bac17102c49
send_addr=2MwCw5Vfw4qwfHCqp3pWXsGM3RnA1Njns5M
fee=0.0001
send_amount=`echo "${redeem_amount}-${fee}" | bc`
#echo ${send_amount}
script_pubkey=76a914b01633747cbc4921912adb98b28cebfbc77662c188ac
private_key=cRYcUiBDPZKpJR268k8PpiMews7Fv84w3sf3t1NsWMJuKDSnUBJu

raw_tx=$(bash cli.bash createrawtransaction  "[{\"txid\":\"${redeem_tx_id}\",\"vout\":0}]" "{\"${send_addr}\":${send_amount}}")
raw_hex_tx=$(bash cli.bash signrawtransaction "${raw_tx}" "[{\"txid\":\"${redeem_tx_id}\",\"vout\":0,\"scriptPubKey\":\"${script_pubkey}\",\"redeemScript\":\"\",\"amount\":${redeem_amount}}]" "[\"${private_key}\"]" | jq  -r '.hex')
echo "${raw_hex_tx}"
bash cli.bash sendrawtransaction "${raw_hex_tx}"

```
OK case
```
bash test_sign_with_amount.bash
0200000001492c1017ac4bc47ca73ff3419fcb2f69c0cd9f160f3c025b073d4a0bfbfbe63e000000006b48304502210091f464e63e59b731cd379ae78341e57fff2da255a3d1f38143b6c28de305ef5102201263f57c41c3a670e692e57940b1966c376ecea4823dd07cada6aafc29b8fc014121032c9f3c2ac952311abb57e70d54ddb061eb954267bfe6117bfdc72c50d3ae406dffffffff01702ec8200000000017a9142b718e29f493a57fc06720dce2d850aa362da4a48700000000
{
  "txid": "8a1ecda874dcc2f421c0e8e96a590a48108ec71b7e8ac43b5643f75a765b4017",
  "hash": "8a1ecda874dcc2f421c0e8e96a590a48108ec71b7e8ac43b5643f75a765b4017",
  "size": 190,
  "version": 2,
  "locktime": 0,
  "vin": [
    {
      "txid": "3ee6fbfb0b4a3d075b023c0f169fcdc0692fcb9f41f33fa77cc44bac17102c49",
      "vout": 0,
      "scriptSig": {
        "asm": "304502210091f464e63e59b731cd379ae78341e57fff2da255a3d1f38143b6c28de305ef5102201263f57c41c3a670e692e57940b1966c376ecea4823dd07cada6aafc29b8fc01[ALL|FORKID] 032c9f3c2ac952311abb57e70d54ddb061eb954267bfe6117bfdc72c50d3ae406d",
        "hex": "48304502210091f464e63e59b731cd379ae78341e57fff2da255a3d1f38143b6c28de305ef5102201263f57c41c3a670e692e57940b1966c376ecea4823dd07cada6aafc29b8fc014121032c9f3c2ac952311abb57e70d54ddb061eb954267bfe6117bfdc72c50d3ae406d"
      },
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 5.49990000,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_HASH160 2b718e29f493a57fc06720dce2d850aa362da4a4 OP_EQUAL",
        "hex": "a9142b718e29f493a57fc06720dce2d850aa362da4a487",
        "reqSigs": 1,
        "type": "scripthash",
        "addresses": [
          "bchtest:pq4hrr3f7jf62l7qvusdeckc2z4rvtdy5sxycpvxrg"
        ]
      }
    }
  ]
}
8a1ecda874dcc2f421c0e8e96a590a48108ec71b7e8ac43b5643f75a765b4017
```

NG case
```
bash test_sign_with_amount.bash
0200000001492c1017ac4bc47ca73ff3419fcb2f69c0cd9f160f3c025b073d4a0bfbfbe63e000000006b48304502210091f464e63e59b731cd379ae78341e57fff2da255a3d1f38143b6c28de305ef5102201263f57c41c3a670e692e57940b1966c376ecea4823dd07cada6aafc29b8fc014121032c9f3c2ac952311abb57e70d54ddb061eb954267bfe6117bfdc72c50d3ae406dffffffff01702ec8200000000017a9142b718e29f493a57fc06720dce2d850aa362da4a48700000000
{
  "txid": "8a1ecda874dcc2f421c0e8e96a590a48108ec71b7e8ac43b5643f75a765b4017",
  "hash": "8a1ecda874dcc2f421c0e8e96a590a48108ec71b7e8ac43b5643f75a765b4017",
  "size": 190,
  "version": 2,
  "locktime": 0,
  "vin": [
    {
      "txid": "3ee6fbfb0b4a3d075b023c0f169fcdc0692fcb9f41f33fa77cc44bac17102c49",
      "vout": 0,
      "scriptSig": {
        "asm": "304502210091f464e63e59b731cd379ae78341e57fff2da255a3d1f38143b6c28de305ef5102201263f57c41c3a670e692e57940b1966c376ecea4823dd07cada6aafc29b8fc01[ALL|FORKID] 032c9f3c2ac952311abb57e70d54ddb061eb954267bfe6117bfdc72c50d3ae406d",
        "hex": "48304502210091f464e63e59b731cd379ae78341e57fff2da255a3d1f38143b6c28de305ef5102201263f57c41c3a670e692e57940b1966c376ecea4823dd07cada6aafc29b8fc014121032c9f3c2ac952311abb57e70d54ddb061eb954267bfe6117bfdc72c50d3ae406d"
      },
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 5.49990000,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_HASH160 2b718e29f493a57fc06720dce2d850aa362da4a4 OP_EQUAL",
        "hex": "a9142b718e29f493a57fc06720dce2d850aa362da4a487",
        "reqSigs": 1,
        "type": "scripthash",
        "addresses": [
          "bchtest:pq4hrr3f7jf62l7qvusdeckc2z4rvtdy5sxycpvxrg"
        ]
      }
    }
  ]
}
error code: -26
error message:
16: mandatory-script-verify-flag-failed (Signature must be zero for failed CHECK(MULTI)SIG operation)

```
