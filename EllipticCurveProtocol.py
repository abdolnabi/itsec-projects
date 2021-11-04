class EllipticCurveProtocol:
    def __init__(self, a=1,b=0,z=1):
        self.a = a
        self.b = b
        self.z = z
        self.s = 0
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.x3 = None
        self.y3 = None
        self.d = None

    def set_base_point_p(self,x1=0,y1=0):
        self.x1 = x1
        self.y1 = y1
        self.p = (x1,y1)

    def set_base_point_q(self,x2= None,y2=None):
        if x2 is None and y2 is None:
            self.x2 = 0
            self.y2 = 0
        else:
            self.x2 = x2
            self.y2 = y2
        self.q = (x2,y2)

    def modInverse(self,a, m):
        for x in range(1, m):
            if (((a % m) * (x % m)) % m == 1):
                return x
        return -1

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
        self.s = int(s_up * self.modInverse(s_down,self.z)) % self.z


    def calc_elliptic_curve_double(self,p):
        x1,y1 = p
        if p ==(0,0):
            return 0,0
        x2 = x1
        y2 = y1
        self.calc_elliptic_curve_s(p,p)
        if self.s is not None:
            x3 = (pow(self.s, 2) - x1 - x2) % self.z
            y3 = (self.s * (x1 - x3) - y1) % self.z
            return x3,y3

    def calc_elliptic_curve_add(self,p,q):
        x1,y1 = p
        x2,y2 = q
        if q == (0,0):
            return p
        self.calc_elliptic_curve_s(p,q)
        if self.s is not None:
            x3 = (pow(self.s, 2) - x1 - x2) % self.z
            y3 = (self.s * (x1 - x3) - y1) % self.z
            return x3,y3

    def multiply_point_ecc(self,d=2):
        d_bin = "{0:b}".format(d)
        p = self.p
        p1=(0,0)
        for d_digit in d_bin:
            p1 = self.calc_elliptic_curve_double(p1)
            if d_digit == '1':
                p1 = self.calc_elliptic_curve_add(p,p1)
            if p1 is None:
                p1 =0
        return p1

if __name__ == "__main__":
    fn = EllipticCurveProtocol(-3,3, 17)
    fn.set_base_point_p(3,2)
    result = fn.multiply_point_ecc(3)
    print(result)