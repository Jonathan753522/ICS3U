#Make:
import math



def factorize(N):
  NA = []
  for J in range(1,N): 
    if (N % J == 0):  
      NA.append(J)
  return NA

print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))

#Parameter:
import math
def factorize(N):
  NA = []
  for J in range(1,N): 
    if (N % J == 0):  
      NA.append(J)
  return NA

try:
  num = int(input("please input a value: "))
  print(factorize(num))
except:  
  print("You Did Not Input A Valid Number")

#Make More:

import math
def factorize(N):
  NA = []
  for J in range(1,N): 
    if (N % J == 0):  
      NA.append(J)
  return NA

def FSum(N):
  SumAmount = 0
  for s in N:
    SumAmount += s
  return SumAmount


try:
  num = int(input("please input a value: "))
  Factors = factorize(num)
  Sum = FSum(Factors)
  print("Factor Sum: %d" % Sum)
  
  if Sum == num:
    print("Factor is Perfect")
    
  if Sum > num:
    print("Factor Is Abundant")
    
  if Sum < num:
    print("Factor Is Deficient")
    
  6
except:
  print("Please Input A Valid Value")
