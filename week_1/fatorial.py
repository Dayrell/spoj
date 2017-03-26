def factorial ( num ):
  fat = 1
  for i in range(2,num+1):
    fat = fat * i
    
  print (fat)
  
n = int(input())
fat = factorial(n) 
