import sys
import os

myString = "09:00:00AM"

def timeConversion(s):
    result = " "
    if myList[3] == "AM":
        if myList[0] == "12":
            result == "00"
        else:
            result = mylist[0]
    else:
        if myList [0] == "12":
            result = "12"
        else:
            result = str(int(myList[0])+12)
            
            print(f"{result = result + ":"+ myList[1] + ":" + myList[2]}")
            return result
    
    
def convert2list (myString):
    # input = hh:mm:ssAM/PM
    #         0123456789
    result = [] # [hh, mm, ss, shift]
    result.append(myString[0:2])
    result.append(myString[3:5]) 
    result.append(myString[6:8]) 
    result.append(myString[8:10])   
    
    return result
