import math


def solve(a, b, c, d):

    if a != 0:
        b = b / a
        c = c / a
        d = d / a

        p = c - ((b ** 2) / 3)
        q = (2 * (b ** 3 / 27)) - (b * c) / 3 + d

        Delta_1 = ((q ** 2) / 4) + ((p ** 3) / 27)

        print("the Delta is", Delta_1)

        if Delta_1 > 0:
            print("There is only one real answer to the equation.")
            x = (-q / 2 + math.sqrt(Delta_1)) ** 1 / 3 + (-q / 2 - math.sqrt(Delta_1)) ** 1 / 3 / (b / 3)
            print(x)
        elif Delta_1 == 0:
            print("There are two real answer to the equation.")
            x1 = (-2 * ((q / 2) ** 1 / 3)) - (b / 3)
            x2 = ((q / 2) ** 1 / 3) - (b / 3)
            print(x1)
            print()
            print(x2)
        elif Delta_1 < 0:
            print("The equation in real numbers has no answer.")

    else:
        print("This is not a cubic equation")
        exit()


a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = int(input('Enter d: '))
solve(a, b, c, d)