# if number is divisible by 3 print fizz if number divisble by 5 print buzz and if divisible by both print fizzbuzz
# and else print the number between 1 to 100

target = 100
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)