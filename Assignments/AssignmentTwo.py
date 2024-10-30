"""
   Author : Jonathan Lee
   Revison date : 29 October 2024
   Program : Yearbook Photo Optimzier
   Description : What ever number you input it finds the optimal perimeter
   VARIABLE DICTIONARY :
     Fullname (String) = person's name
     height (double) = person's height
     Lastname (String) = string object for entering the last-names
     Firstname (String) = string object for entering the *first-names
     B (String) = a variable for ignoring the first line in the file
     sum (double) = variable for the total sum of the heights
     avg (double) = variable for the average of all heights
     count (int) = the number of people averaged
"""

import math

#Functions

def PhotoFactors(N):
    Photonum = []
    mnum = math.floor(math.sqrt(N))
    for Xaxis in range(1,mnum + 1): 
        if N % Xaxis == 0:  
            Photonum.append(Xaxis)
  
    return Photonum

#Calculates Perimeter
def perim(N):
    Factor = PhotoFactors(N)
    Xaxis = 1
    for num in Factor:
        if num > Xaxis:
            Xaxis = num 
    Yaxis = N / Xaxis
    perimeter = 2 * (Xaxis + Yaxis)
    print("Minimum perimeter is %d with dimensions: %d x %d" % (perimeter, Xaxis, Yaxis))
    
def CheckNeg(N):
    if (photooutput < 0):
        print("%d is not a valid number of photos" % (N))
        print("Please input a positive number")
    elif N > 0:
        perim(N)

#Printing Statments/Loop
print("Welcome to the school yearbook program!")

done = False

#While Loop

while (done != True):
    try:
        userinp = (input("Please Input A Number Of Photographs: "))
        if (userinp.lower() == "done") or (userinp == "0"):
            print("Goodbye!")
            done = True
            break
        if not isinstance(userinp, int):
            photooutput = int(userinp)
        CheckNeg(photooutput)
    except:
        print("%s is not a valid number of photos" % (userinp))

