"""
   Author : Jonathan Lee
   Revison date : 29 October 2024
   Program : Yearbook Photo Assignment
   Description : What ever number you input it finds the optimal perimeter
   VARIABLE DICTIONARY :
     userinp (String) = Users input
     Photo_output (Int) = Userinp converted to an integer
     Xaxis (int) = X axis used to find the perimeter
     Yaxis (int) = Y axis used to find the perimeter
     done (bool) = Boolean that stops the loop when entered
     perimeter (int) = Total Perimeter of all photos
     Photonum (list) = list of photo factors
     mnum (int) = Minimun Number Of Photos
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
    
#Checks To See If Input Is Negative
def CheckNeg(N):
    if (N < 0):
        print("%d is not a valid number of photos" % (N))
        print("Please input a positive number")
    elif (N == 0):
        print("%d is not a valid number of photos" % (N))
    elif N > 0:
        perim(N)

#Printing Statments/Loop
print("Welcome to the school yearbook program!")

done = False

#While Loop
while (done != True):
    try:
       #User input 
        userinp = (input("Please Input A Number Of Photographs: "))
        if (userinp.lower() == "done"):
            print("Goodbye!")
            done = True
            break
        if done == False:
            photo_output = int(userinp)
        CheckNeg(photo_output)
    except:
        print("%s is not a valid number of photos" % (userinp))
