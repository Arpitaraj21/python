# bmi calculator using if else

height = float(input())
weight = int(input())

bim = weight / (height * height)
if bim < 18:
    print(f"your bim is {weight}, you are underweight")
if bim< 18 and bim < 25:
    print(f"your bim is {weight}, have a normal weight")
if bim >= 25 and bim <30:
    print(f"your bim is {weight}, you are slightly overweight")
if bim >= 30  and bim < 35:
    print(f"your bim is {weight}, you are obese")
if bim >= 35:
    print(f"your bim is {weight}, you are clinically obese")