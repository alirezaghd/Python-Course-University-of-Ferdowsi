class Zaman():
    def __init__(self,hour=0,minute=None,second = 1):

        self.h = hour
        self.m = minute
        self.s = second

    def add(self,other):

        result = Zaman()

        result.h = self.h + other.h
        result.m = self.m + other.m
        result.s = self.s + other.s

        if result.s >= 60 :
            result.s -= 60
            result.m +=1
        
        if result.m >= 60 :
            result.m -= 60
            result.s +=1

        return result

    def sub(self , other):
        result = Zaman()

        result.h = self.h - other.h
        result.m = self.m - other.m
        result.s = self.s - other.s

        if result.s < 0:
            result.s += 60
            result.m -= 1
        if result.m < 0:
            result.m += 60
            result.h -= 1

        return result

    def time_To_Secend(self):

        result = Zaman()

        hour = self.h
        minute = self.m
        second = self.s
        h = hour * 3600
        m = minute * 60
        result = h + m + second
        return result

    


    def show(self):
        print(self.h,":",self.m,":",self.s)



t1 = Zaman(10,30,4)
t2 = Zaman(2,45,10)
t1.show()
t2.show()

t3 = t1.add(t2)
t3.show()

t4 = t1.sub(t2)
t4.show()

print('Seconds: ', t1.time_To_Secend())