from EllipticCurveMath import EllipticCurveMath

class EllipticCurveProtocol:
    def __init__(self, a=0, b=0, P=0, N=0, Gx=0, Gy=0, name=''):
        self.a = a
        self.b = b
        print ("All variables are set successfully!")
        self.z = P
        self.s = 0
        self.Xp = Gx
        self.Yp = Gy
        self.p =(self.Xp,self.Yp)
        self.order = N
        self.Xq = None
        self.Yq = None
        self.x3 = None
        self.y3 = None
        self.d = None

    def set_base_point_p(self):
        self.p = (self.Xp, self.Yp)



    def set_base_point_q(self, Xq= None, Yq=None):
        self.Yq = Yq
        self.Xq = Xq
        self.q = (self.Xq, self.Yq)



    def isoncurve(self):
        if not 0 <= self.Xp <= self.z - 1:
            return False
        if not 0 <= self.Yp <= self.z - 1:
            return False
        if (self.Yp**2 - (self.Xp**3 + self.a * self.Xp + self.b)) % self.z != 0:
            return False
        return True

if __name__ == "__main__":
    bb = EllipticCurveProtocol(
        name="secp256k1",
        a=0,
        b=649016698881877847465653473434873449019011128250537183611,
        P=6277101735386680763835789423207666416083908700390324961279,
        N=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
        Gx=602046282375688656758213480587526111916698976636884684818,
        Gy=174050332293622031404857552280219410364023488927386650641
    )
    bb.calc_elliptic_curve_s()
    print(bb.s)
    print("Do nothing")
