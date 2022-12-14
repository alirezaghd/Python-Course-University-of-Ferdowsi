print("مثلث")

a = int((input("insert first slide")))
b = int((input("insert second slide")))
c = int((input("insert third  slide")))

if a < b + c and b < c + a and c < a + b :
    print("اندازه هر ضلع کوچکتر از جمع اندازه دو ضلع دیگر است") 
else:
    print("اندازه هر ضلع کوچکتر از جمع اندازه دو ضلع دیگر نیست.") 


