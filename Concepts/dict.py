# Dictonary and Methods
# Dict is mutable

dict1 = {"good": "something pleasant", "fetch": "to bring", "1": "number 1" }
print(dict1["good"])

marks = {"Arpita": "89", "Swati": "99", "Raj": "76", "Sweta": "45", "Sabita": "95"}

print(marks["Sabita"])
marks["Priyanka"] = 34
print(marks)

# agar key nahi hai toh error nahi aayega None return hoga
print(marks.get("Priyanka"))

print(marks.keys())
print(marks.values())
print(marks.items())