# String and String methods

name = "aRPITa"
last_name = 'Raj'
number = 7
print(f"My name is {name} {last_name} ")

# Slicing  # [0: n-1]

print(name[0:3])
# O/P : Arp

print(name[1:3])
# O/P : rp

##### STRING METHODS

print(name.upper())
print(name.capitalize())
print(name.count("r"))
print(name.isalnum())
#print(number.isnumeric())
print(name.casefold()) # converts all the capital letters to small letters
print(name.center(2)) #need to understand later


# <---- More on Strings

a1 = "Arpita"
a2 = 'Arpita'
a3 = '''Arpita'''
print(type(a3))
print(a1, a2, a3)


#mutliline string

a4 = ''' Arpita
is a good 
girl.
'''
print(a4)

a5 = 'Arpita'   \
      'is a good girl'

print(a5)

#NOTE -> String is immutable isliye har baar methods use karne se pycharm
# ek new string banata hai but that is not the case with list agar koi chiz
# change hota hai toh vo direactly uss list me change hota hai