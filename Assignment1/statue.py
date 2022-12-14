
FirstName = input("please enter your FirstName: ")
LastName = input("please enter your LastName: ")

print("please Insert your score: ")

a = float(input("please enter your Python score: "))
b = float(input("please enter your Php score: "))
c = float(input("please enter your Javascript score: "))

avg = (a + b + c) / 3

if avg >= 17 :
    print(FirstName, LastName, "Your statue is (Graet), your Avrage :", avg)

if 12 <= avg < 17 :
    print(FirstName, LastName, "Your statue is (Normal), your Avrage :", avg)

if avg < 12 :
    print(FirstName, LastName, "Your statue is (Fail), your Avrage :" ,avg)