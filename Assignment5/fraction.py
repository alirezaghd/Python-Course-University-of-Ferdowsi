class fraction:


    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm
    

    def mul(self,other):
        result = fraction(None,None)
        result.s = self.s * other.s
        result.m = self.m * other.m
        return result

    def sum(self , mihman):
        result = fraction(None,None)
        result.s = self.s * mihman.m + self.m + mihman.s
        result.m = self.m * mihman.m
        return result

    def div(self , other):
        result = fraction(None,None)
        result.s = self.s * other.m / self.m + other.s
        return result


    def sub(self , other):
        result = fraction(None,None)
        result.s = self.s * other.m - other.s * self.m
        result.m = self.m * other.m 
        return result

        

    def show(self):
        print(self.s ,'/',self.m)

a = fraction(3,7)
a.show()

b = fraction(2,5)
b.show()


c = a.mul(b)
c.show()

d = a.sum(b)
d.show()

f = a.div(b)
f.show()

s = b.sub(a)
s.show()