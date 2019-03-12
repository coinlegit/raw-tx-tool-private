wif='cPaPiXu54qDEMg5UMyXmKZY8ikb12aZ6JJyzdRZF2CEQY252A9LP'
#bx wif-to-ec L21LJEeJwK35wby1BeTjwWssrhrgQE2MZrpTm2zbMC677czAHHu3
bx wif-to-ec $wif

#entropy[seed] to priv 
echo "a76e98bda0269269a3a2bbc98108ac6cc614c54b94d48f502745b5e74eaff613" | bx ec-new

echo "a76e98bda0269269a3a2bbc98108ac6cc614c54b94d48f502745b5e74eaff613" | bx ec-new | bx ec-to-public | bx ec-to-address



