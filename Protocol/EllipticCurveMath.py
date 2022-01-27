class EllipticCurveMath:
    def __init__(self, p,a , z, d=0 ,q=None ):
        self.d = d
        self.p = p
        self.z = z
        self.a = a
        self.q = q

    @staticmethod
    def modInverse(a, m):
        a = a% m
        if EllipticCurveMath.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

        return u1 % m
    @staticmethod
    def gcd(a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def calc_elliptic_curve_s(self,p,q):
        x1,y1 = p
        x2,y2 = q
        if (x2 == x1 and y2 == y1) or (x2 == None and y2==None):
            s_up = ( 3 * pow(x1, 2) + self.a ) % self.z
            s_down = (2 * y1) % self.z
            if s_up <0 and s_down <0:
                s_up *= -1
                s_down *= -1
        else:
            s_up = y2 - y1 % self.z
            s_down = x2 - x1 % self.z
            if s_up <0 and s_down <0:
                s_up *= -1
                s_down *= -1
        if s_down == 0:
            self.s = None
            return
        s = s_up * pow(s_down,-1,self.z)
        self.s = s % self.z

    def calc_elliptic_curve_double(self,p1):
        x1,y1 = x2,y2 =p1
        if p1 == (0,0):
            return (0,0)
        self.calc_elliptic_curve_s((x1,y1), (x2,y2))
        if self.s is not None:
            x3 = (pow(self.s, 2) - x1 - x2) % self.z
            y3 = (self.s * (x1 - x3) - y1) % self.z
            return x3,y3

    def calc_elliptic_curve_add(self,p1):
        x1,y1 = self.p
        x2,y2 = p1
        if p1 == (0,0):
            return self.p
        self.calc_elliptic_curve_s(self.p, p1)
        if self.s is not None:
            x3 = (pow(self.s, 2) - x1 - x2) % self.z
            y3 = (self.s * (x1 - x3) - y1) % self.z
            return x3,y3

    def multiply_point_ecc(self):
        d_bin = "{0:b}".format(self.d)
        p1=(0,0)
        for d_digit in d_bin:
            p1 = self.calc_elliptic_curve_double(p1)
            if d_digit == '1':
                p1 = self.calc_elliptic_curve_add(p1)
            if p1 is None:
                p1 =0
        return p1