# FILE I/O

s = "Hello, how are you"

# with open("text.txt", "w") as f:
#     f.write(s)
#
# fp = open("text.txt", "w")
# fp.write(s)
# fp.close()

 # Reading a file

# with open("text.txt", "r") as f:
#     R = f.read()
#     print(R)

#
# f = open("text.txt", "r")
# s = f.read()
# print(s)
# f.close()


# Appending to a file

with open("text.text", "a") as f:
    f.write("What about you?")