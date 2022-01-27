import hashlib
from select import select

from EllipticCurveProtocol import EllipticCurveProtocol
from EllipticCurveMath import EllipticCurveMath
from RandomGenerator import RandomGenerator
class ECDSA_Signature:
    def __init__(self):
        #self.d = random.randrange(0,q)
        self.secp256k1 = EllipticCurveProtocol(
            name="secp256k1",
            a=0,
            b=649016698881877847465653473434873449019011128250537183611,
            P=6277101735386680763835789423207666416083908700390324961279,
            N=115792089237316195423570985008687907852837564279074904382605163141518161494337,
            Gx=602046282375688656758213480587526111916698976636884684818,
            Gy=174050332293622031404857552280219410364023488927386650641,
        )

    def calculate_keys(self):
        print("The calculation of Private key started")
        private_key = RandomGenerator.randgen(upper_bound=self.secp256k1.order)
        print("private key is:", private_key)
        curve = EllipticCurveMath(d=private_key, p=(self.secp256k1.Xp, self.secp256k1.Yp),a=self.secp256k1.a,z=self.secp256k1.z)
        B = curve.multiply_point_ecc()
        public_key = {
            "p_modulus": self.secp256k1.z,
            "Coefficients": (self.secp256k1.a,self.secp256k1.b),
            "Order": self.secp256k1.order,
            "A": (self.secp256k1.Xp, self.secp256k1.Yp),
            "B": B
        }
        print(str(public_key))
        return private_key,public_key

    def sign_msg(self,msg,priv_key):
        KE = RandomGenerator.randgen(upper_bound=self.secp256k1.z)
        curve1 = EllipticCurveMath(d=KE, p=(self.secp256k1.Xp, self.secp256k1.Yp), a=self.secp256k1.a,z=self.secp256k1.order)
        R = curve1.multiply_point_ecc()
        r = R[0]
        hx = int(hashlib.sha256(msg.encode()).hexdigest(), 16)
        s = ((hx + priv_key * r) * pow(KE,-1, self.secp256k1.order)) % self.secp256k1.order
        return  r,s


    def verify_msg(self,r,s,msg,pub_key):

        z = pub_key["p_modulus"]
        a,b = pub_key["Coefficients"]
        q = pub_key["Order"]
        A = pub_key["A"]
        B = pub_key["B"]
        w = pow(s, -1,q)
        hx = int(hashlib.sha256(msg.encode()).hexdigest(), 16)
        u1 = (w *  hx) % q
        u2 = (w*r) % q
        curve1 = EllipticCurveMath(d=u1, p=A, a=a,z=z)
        u1A = curve1.multiply_point_ecc()
        curve1 = EllipticCurveMath(d=u2, p=B, a=a, z=z)
        u2B = curve1.multiply_point_ecc()
        curve1 = EllipticCurveMath(p=u1A, a=a, z=z)
        P = curve1.calc_elliptic_curve_add(u2B)
        Px = P[0] % q
        r = r % q
        if Px == r:
            print("Voala! The signature is valid")
        else:
            print("Sorry! The signature is invalid")



    def display_initial_value_state(self):
        if self.secp256k1.isoncurve():
            print("The point is on curve")

if __name__ == "__main__":
    A = ECDSA_Signature()
    A.display_initial_value_state()
    priv_key, pub_key = A.calculate_keys()
    r,s = A.sign_msg(msg="Hey this is me!", priv_key=priv_key)
    A.verify_msg(msg="Hey this is me!",r=r,s=s, pub_key=pub_key)
