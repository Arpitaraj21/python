# Match Case
# match case is a new edition python 3.10

a = int(input("Enter a number: "))

match a:
    case 1:
        print('case 1')
    case 2:
        print('case 2')
    case 3:
        print('case 3')
    case 4:
        print('case 4')
    case _:
        print('no case found')


# Q) Write a python program to print table pf a number which lies between 1 and 10


def print_table(number):
    match number:
        case 1:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i} ")
        case 2:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 3:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 4:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 5:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 6:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 7:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 8:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 9:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 10:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case _:
            print("Case not found")

number = int(input("Enter a number between 1 and 10: "))
print_table(number)