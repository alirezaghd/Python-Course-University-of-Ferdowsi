import random

Array = []
n = int(input("please insert number for len List: "))
while True:
    num = random.randint(0, n)

    if num not in Array :
        Array.append(num)
    
    
    if len(Array) == n :
        print(Array)
        break
    

    