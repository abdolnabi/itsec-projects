import random
from .EllipticCurveMath import EllipticCurveMath
#y^2=x^3+A*x+B

class EllipticCurveProtocol:
    def __init__(self, a, b, P, N, Gx, Gy, name,nistName=None):
        weierstrass_approach = 4 * pow(a, 3) + 27 * pow(b, 2)
        if weierstrass_approach:
            self._a = a
            self._b = b
            print ("All variables are set successfully!")
        else:
            ValueError("a and b do not meet WeierStrass approach! please recheck!!")
        self.z = P
        self.s = 0
        self.Xp = Gx
        self.Yp = Gy

        self.Xq = None
        self.Yq = None
        self.x3 = None
        self.y3 = None
        self.d = None

    def set_base_point_p(self, Xp=0, Yp=0):
        self.Xp = Xp
        self.Yp = Yp
        self.p = (Xp, Yp)

    def set_base_point_q(self, Xq= None, Yq=None):
        if Xq is None and Yq is None:
            self.Xq = 0
            self.Yq = 0
        else:
            self.Xq = Xq
            self.Yq = Yq
        self.q = (Xq, Yq)

    def calc_elliptic_curve_s(self,p,q):
        x1,y1 = p
        x2,y2 = q
        if x2 == x1 and y2 == y1:
            s_up = 3 * pow(x1, 2) + self.a
            s_down = 2 * y1
        else:
            s_up = y2 - y1 % self.z
            s_down = x2 - x1 % self.z
        if s_down == 0:
            self.s = None
            return
        self.s = int(s_up * EllipticCurveMath.modInverse(s_down,self.z)) % self.z

    def isoncurve(self, p):
        """
        verifies if a point is on the curve
        """
        return not p or (p[1] ** 2 == p[0] ** 3 + self.a * p[0] + self.b)

if __name__ == "__main__":
    print("1")
