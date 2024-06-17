import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"
user_email = input("Enter your Email: ")

if re.search(email_condition, user_email):
    print("Correct Email")
else:
    print("Wrong Email")





#group of charcaters dene ke liye [] isko use karte hai
# + ka join karne ka kaam karta hai
# \ jab bhi hm kisi char ko search karte hai
# ? yeh batata hai ki at a time ek hi hona chahiye jiske baad lagayenge
# \w ka kaam hai string me diye hue special character ko search karna
# \W diye hue condition ka ulta kaam karta
# agar koi condition particaular position ke upar search karne ke liye {}
# piche se use karne ke liye $ sign ka use karna padta hai