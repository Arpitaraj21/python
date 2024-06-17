height = input()
weight = input()

weight_as_integer = int(weight)
height_as_float = float(height)

bim = int(weight_as_integer / height_as_float ** 2)

print(bim)