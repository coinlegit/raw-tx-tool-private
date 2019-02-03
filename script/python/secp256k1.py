# -*- coding: utf-8 -*-
#import Crypto.Hash.SHA256 as sha256
#import hashlib


# specs for Bitcoin's curve - the secp256k1
# y2 = x^3 + 7

P = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 #
# n: 115792089237316195423570985008687907852837564279074904382605163141518161494337
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 #
A = 0; B = 7 # These two defines the elliptic curve. y^2 = x^3 + A * x + B
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx,Gy) # This is generator point/base point.

def mgcd(a,b):
     """Returns (gcd, x, y, s, t) where
     gcd is the greatest common divisor of a and b, with the sign of b
     if b is nonzero, and with the sign of a if b is 0;
     the numbers x,y, s, t are such that
        gcd = xa+yb
          0 = sa+tb
     and abs(xt-ys) = 1
     Otherwise put: the determinant of matrix (hence m in name)
         x y
         s t
     has magnitude 1, and multiplied by column vector
            a
            b
     is column vector
            gcd
            0
     """
     prevx, x = 1, 0;  prevy, y = 0, 1
     while b:
         q, r = divmod(a, b)
         x, prevx = prevx - q*x, x
         y, prevy = prevy - q*y, y
         a, b = b, r
     return a, prevx, prevy, x, y

def modinv2(a, n=N):
    (gcd, x, y, s, t ) = mgcd(a, N)
    return x % N

def modinv(a,n=N):
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n


def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

#Uncompressed public key is:
#0x04 + x-coordinate + y-coordinate

#Compressed public key is:
#0x02 + x-coordinate if y is even
#0x03 + x-coordinate if y is odd
#y^2 mod p = (x^3 + 7) mod p
#y^2 mod p = (x^3 + 7) mod p
#y mod p = +-(x^3 + 7)^((p+1)/4) mod p
def get_uncompressedkey(compressed_key):
    y_parity = int(compressed_key[:2]) - 2
    x = int(compressed_key[2:], 16)
    a = (pow_mod(x, 3, p) + 7) % p
    y = pow_mod(a, (p+1)//4, p)
    if y % 2 != y_parity:
        y = -y % p
    return (x, y)

#multiply scalar calculation
# p1(x1,y1),p2(x2,y2) ->p3(x3,y3)を求める
# lambda
#     y2-y1
# λ= -------  [if (x1,y1)≠(x2,y2)]
#     x2-x1
# x3 = λ^2-x1-x2
# y3 = λ(x1-x3)-y1

#    3x1^2+a
# λ= --------  [if (x1,y1)＝(x2,y2)]
#     2y1
# x3= λ^2-x1-x1
# y3= λ(x1-x3)-y1
#

def ECadd(a,b):
    Lambda = ((b[1]-a[1]) * modinv(b[0]-a[0],P)) % P
    x = (Lambda*Lambda-a[0]-b[0]) % P
    y = (Lambda*(a[0]-x)-a[1]) % P
    return (x,y)

def ECdouble(a):
    Lambda = ((3*a[0]*a[0]+A) * modinv((2*a[1]),P)) % P
    x = (Lambda*Lambda-2*a[0]) % P
    y = (Lambda*(a[0]-x)-a[1]) % P
    return (x,y)

def ECmultiply(G,ScalarHex):
    if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=G
    for i in range (1, len(ScalarBin)):
        Q=ECdouble(Q);
        if ScalarBin[i] == "1":
            Q=ECadd(Q,G);
    return (Q)

def GetPubkeyFromPrivkey(privkey):
    PublicKey=ECmultiply(G, privkey)
    if PublicKey[1] % 2 == 1: # If the Y value for the Public Key is odd.
        return "03"+str(hex(PublicKey[0])[2:-1]).zfill(64)
    else: # Or else, if the Y value is even.
        return"02"+str(hex(PublicKey[0])[2:-1]).zfill(64)

def GetPubkeyFromPoint(Point):
    if Point[1] % 2 == 1: # If the Y value for the Public Key is odd.
        return "03"+str(hex(Point[0])[2:-1]).zfill(64)
    else: # Or else, if the Y value is even.
        return"02"+str(hex(Point[0])[2:-1]).zfill(64)

#Compressed public key is:
#0x02 + x-coordinate if y is even
#0x03 + x-coordinate if y is odd
#y^2 mod p = (x^3 + 7) mod p
#y^2 mod p = (x^3 + 7) mod p
#y mod p = +-(x^3 + 7)^((p+1)/4) mod p
def GetUncompressedkey(compressed_key):
    y_parity = int(compressed_key[:2]) - 2
    x = int(compressed_key[2:], 16)
    a = (pow_mod(x, 3, P) + 7) % P
    y = pow_mod(a, (P+1)//4, P)
    if y % 2 != y_parity:
        y = -y % P
    return (x, y)

def ParseElement(hex_str, offset, element_size):
    """
    :param hex_str: string to parse the element from.
    :type hex_str: hex str
    :param offset: initial position of the object inside the hex_str.
    :type offset: int
    :param element_size: size of the element to extract.
    :type element_size: int
    :return: The extracted element from the provided string, and the updated offset after extracting it.
    :rtype tuple(str, int)
    """

    return hex_str[offset:offset+element_size], offset+element_size
'''
DER ASN1-encoding

    30     len(z)     02     len(r)     r        02      len(s)    s     hashtype
|--------|--------|--------|--------|--------|--------|--------|--------|--------|
     1       1         1        1      32-33      1        1      32-33     1

30
44
02
20 32/33bytes
02
20 32/33bytes
01
'''
def ParseSignature(hex_sig):
    """
    Extracts the r, s and ht components from a Bitcoin ECDSA signature.
    :param hex_sig: Signature in  hex format.
    :type hex_sig: hex str
    :return: r, s, t as a tuple.
    :rtype: tuple(str, str, str)
    """

    offset = 0
    # Check the sig contains at least the size and sequence marker
    assert len(hex_sig) > 4, "Wrong signature format."
    sequence, offset = ParseElement(hex_sig, offset, 2)
    # Check sequence marker is correct
    assert sequence == '30', "Wrong sequence marker."
    signature_length, offset = ParseElement(hex_sig, offset, 2)
    # Check the length of the remaining part matches the length of the signature + the length of the hashflag (1 byte)
    #assert len(hex_sig[offset:])/2 == int(signature_length, 16) + 1, "Wrong length."
    assert len(hex_sig[offset:])/2 == int(signature_length, 16) , "Wrong length."
    # Get r
    marker, offset = ParseElement(hex_sig, offset, 2)
    assert marker == '02', "Wrong r marker."
    len_r, offset = ParseElement(hex_sig, offset, 2)
    len_r_int = int(len_r, 16) * 2   # Each byte represents 2 characters
    r, offset = ParseElement(hex_sig, offset, len_r_int)
    # Get s
    marker, offset = ParseElement(hex_sig, offset, 2)
    assert marker == '02', "Wrong s marker."
    len_s, offset = ParseElement(hex_sig, offset, 2)
    len_s_int = int(len_s, 16) * 2  # Each byte represents 2 characters
    s, offset = ParseElement(hex_sig, offset, len_s_int)
    # Get ht
    # ht, offset = ParseElement(hex_sig, offset, 2)
    assert offset == len(hex_sig), "Wrong parsing."

    #return r, s, ht
    return r, s

