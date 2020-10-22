
class MyFraction:
    def __init__(self, numerator, denominator):
        ### your code here ###
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        ### do not edit here ###
        return '{}/{}'.format(self.numerator,self.denominator)


    def negate(self):
        ### your code here ###
        return -self

    def inverse(self):
        ### your code here ###
        return MyFraction(self.denominator,self.numerator)

    def reduction(self):
        ### do not edit here ###
        a = self.numerator
        b = self.denominator
        if a < b: 
            (a, b) = (b, a)
        while b != 0:
            (a, b) = (b, a % b)
        self.numerator = int(self.numerator / a)
        self.denominator = int(self.denominator / a)
        return self


    def __add__(self, frac):
        ### do not edit here ###
        if isinstance(frac, int):
            frac = MyFraction(self.denominator*frac, self.denominator*frac)
        numerator = (self.numerator * frac.denominator) + (self.denominator * frac.numerator)
        denominator = self.denominator * frac.denominator
        return MyFraction(numerator, denominator).reduction()

    def __sub__(self, frac):
        ### your code here ###
        if isinstance(frac, int):
            frac = MyFraction(self.denominator+frac, self.denominator)
        numerator = self.numerator*frac.denominator-self.denominator*frac.numerator
        denominator = self.denominator*frac.denominator
        return MyFraction(numerator, denominator).reduction()

    def __mul__(self, frac):
        ### do not edit here ###
        if isinstance(frac, int):
            frac = MyFraction(self, self.denominator*frac, self.denominator*frac)
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        return MyFraction(numerator, denominator).reduction()


    def __truediv__(self, frac):
        ### your code here ###
        if isinstance(frac, int):
            frac = MyFraction(self, self.denominator*frac, self.denominator*frac)
        numerator = self.numerator * frac.denominator
        denominator = self.denominator * frac.numerator
        return MyFraction(numerator, denominator).reduction()


a = MyFraction(1,2)
b = MyFraction(3,5)
x = b - a 
print('x={}, b={}, a={}'.format(x,b,a))

c = x + 1
d = x + b
y = d / c
print('y={}, d={}, c={}'.format(y,d,c))
