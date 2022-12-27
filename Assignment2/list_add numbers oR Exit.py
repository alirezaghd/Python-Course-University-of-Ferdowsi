print("This program receives numbers from the user until the user enters the ''Exit'' phrase and finally displays the sum of the numbers to the user.")
list = []

while True:
    num = input("please insert numbers Or 'Exit': ")
    if num == 'Exit':
        sum_numbers = sum(list)
        print("Yout Insert number is :",list)
        print("Yout Total number is :",sum_numbers)
        break
    list.append(int(num))

    