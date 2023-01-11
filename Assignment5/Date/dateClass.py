class Date():
    def __init__(self,day = None,month = None,year = None):
        self.y = year
        self.m = month
        self.d = day

    def isValidDate(self):
        if self.y > 9999 or self.y < 1 or self.m > 12 or self.m < 1 or self.d > 30 or self.d < 1:
            return False
        else:
            return True

    def add(self,other):
        result = Date(None,None,None)
        result.d = self.d + other.d
        result.m = self.m + other.m
        if result.d >30:
            result.d -= 30
            result.m +=1
        result.y = self.y + other.y
        if result.m > 12:
            result.m -= 12
            result.y += 1
        return result

    def getMonthName(self):
        month = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
        print(month[self.m-1])

    def isLeapYear(self):
        if self.y % 4 == 3:
            print('True')
        else:
            print('False')

    def sub(self,other):
        result = Date(None,None,None)
        result.d = self.d - other.d
        result.m = self.m - other.m
        result.y = self.y - other.y

        if result.d < 1:
            result.d += 30
            result.m -= 1
        
        if result.m < 1 :
            result.m += 12
            result.y -= 1

        if result.m == 0:
            result.m = 12

        return result 

    


    def show(self):
        print(self.y,'/',self.m,'/',self.d)