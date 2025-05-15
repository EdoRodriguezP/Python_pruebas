import sys
import os

hora = "12:00:00pm"
myString = hora.lower()
result = ""

def conver2list (hora):
    return[
        myString[0:2],  # hh
        myString[3:5],   # mm
        myString[6:8],   # ss
        myString[8:10]   # AM/PM      
    ]
    

if myString[3] == "am":
        if myString[0] == "12":
            result == "00"
        else:
            result = myString[0]
else:
        if myString [0] == "12":
            result = "12"
        else:
            result = str(int(myString[0])+12)
            
print(f"{result}:{myString[1]}:{myString[2]}")


print(hora)
print(myString)







'''
def timeConversion(s):
    result = ""
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
            
            result = result + ":"+ myList[1] + ":" + myList[2]
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
'''