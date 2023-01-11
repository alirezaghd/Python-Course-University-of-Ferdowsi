from dateClass import Date
import time


while True:
    print('1 - Sum two Date\n2 - Sub two Date\n3 - Get month\n4 - Age\n0 - Exit')  
    choice = int(input('Please Enter number : '))

    print('Enter the First Date: {dd/mm/yyyy}')
    d1 = int(input('Please Enter the day(1) :'))
    m1 = int(input('Please Enter the month(1) :'))
    y1 = int(input('Please Enter the year(1) :'))
    a = Date(d1,m1,y1)
    
        
    if choice == 1 or choice == 2:
            
            
        print('Enter the second Date:{dd/mm/yyyy} ' )
            
        d2 = int(input('Please Enter the day(2) :'))
        m2 = int(input('Please Enter the month(2) :'))
        y2 = int(input('Please Enter the year(2) :'))
        b = Date(d2,m2,y2)
    if choice == 1:
        a.add(b).show()
    elif choice == 2:
        a.sub(b).show()
        
    elif choice == 3:
        a.getMonthName()

    elif choice == 4:

        named_tuple = time.localtime() 
        Todey = time.strftime("%d/%m/%Y", named_tuple)
        
        print('Todey is',Todey)
        birthDay = a
        Todey = Date(day=named_tuple[2] , month=named_tuple[1] , year=named_tuple[0] )
        

        age = birthDay.sub(Todey)
        age.show()

    elif choice == 9:
        exit()