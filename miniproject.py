from time import *
import random as r 
print(time())
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error +1
        except :
            error =error +1
    return error
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)
while True:
    ck = input("Are you ready to calculate your typing speed?:(Yes/No):")
    if ck == "Yes":
        test=["Python is a high-level (human-readable) programming language that is processed by the Python interpreter to produce results. Python includes a comprehensive standard library of tested code modules that can be easily incorporated into your own progress."]
        test1 = r.choice(test)
        print ("********** typing speed **********")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter:")
        time_2 = time()
        print('Speed:',speed_time(time_1,time_2,testinput),"words/sec")
        print("Error:",mistake(test1,testinput))
    elif ck == "No":
        print("Thankyou for visiting")
        break
    else:
        print("Wrong input")
        
    
        
