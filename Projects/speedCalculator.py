from time import *
import random as r


def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
            else:
                pass
        except:
            error += 1
    return error        
        
        
def speed_time(time_start, time_end, userinput):
    time_delay =  time_end - time_start
    time_Round = round(time_delay, 2)
    speed = len(userinput) / time_Round
    return round(speed)
   
   
   
while True:
    ck = input("ready to test : yes / no :")    
    if ck == 'yes':
        test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea."
        "my name is arpita raj", "welcome to my github"]

        test1 = r.choice(test)
        print("*****typing speed calculator*****")
        print(test1)
        print()
        print()

        time_1 = time()
        user_input = input("Enter the text you see on your screen to calculate the speed: ")

        time_2 = time()

        print("Speed: ",  speed_time(time_1, time_2, user_input), "w/sec")
        print('error: ', mistake(test1, user_input))

    elif ck == 'no':
        print("Thankyou")
        break
    else:
        print("Wrong input")