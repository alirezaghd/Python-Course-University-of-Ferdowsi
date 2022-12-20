import random

print('"""Number guessing game"""')
pc_number = random.randint(0,20)
print("You only have 10 chances")

count = 0

for i in range(10):
    user_number = int(input("Enter number between 0 and 20 :"))
    if pc_number == user_number :
        print("you Winner")
        print (f"You could win by guessing {count} times")
        break
    if user_number > pc_number :
        print("boro payinTar")
        count += 1

    if user_number < pc_number :
        print("boro BalaTar")
        count += 1

    if i >= 9 :
        print("you loser")
        break
