import random
while True:
    t = random.randint(1, 6)
    if t == 6:
        print("your tas number : ",t)
        print('tas is 6 and you have another chance')
    else:
        print("your tas number : ",t)
        print('tas is not 6 and end of your chance')
        break
