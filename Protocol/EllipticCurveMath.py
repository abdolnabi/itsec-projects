class EllipticCurveMath:

    def modInverse(self,a, m):
        for x in range(1, m):
            if (((a % m) * (x % m)) % m == 1):
                return x
        return -1


    def calc_elliptic_curve_double(self,p,s=1,z=1):
        x1,y1 = p
        if p ==(0,0):
            return 0,0
        x2 = x1
        y2 = y1
        if s is not None:
            x3 = (pow(s, 2) - x1 - x2) % z
            y3 = (s * (x1 - x3) - y1) % z
            return x3,y3

    def calc_elliptic_curve_add(self,p,q,s=1,z=1):
        x1,y1 = p
        x2,y2 = q
        if q == (0,0):
            return p
        if s is not None:
            x3 = (pow(s, 2) - x1 - x2) % z
            y3 = (s * (x1 - x3) - y1) % z
            return x3,y3

    def multiply_point_ecc(self,d=2,p=(0,0)):
        d_bin = "{0:b}".format(d)
        p1=(0,0)
        for d_digit in d_bin:
            p1 = self.calc_elliptic_curve_double(p1)
            if d_digit == '1':
                p1 = self.calc_elliptic_curve_add(p,p1)
            if p1 is None:
                p1 =0
        return p1