import random
import PrimeFinder
from .EllipticCurveProtocol import EllipticCurveProtocol
class ECDSA_Signature:
    def __init__(self,p=2,q=3,):
        self.d = random.randrange(0,q)
        secp256k1 = EllipticCurveProtocol(
            name="secp256k1",
            A=0x0000000000000000000000000000000000000000000000000000000000000000,
            B=0x0000000000000000000000000000000000000000000000000000000000000007,
            P=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
            N=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
            Gx=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
            Gy=0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
        )
        secp256k1.set_base_point_p()
