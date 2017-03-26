# Fábio Dayrell Ferreira Martins Rosa | 2011054383
# Overflow (FATORIA2)
# Realizo a soma dos termos da sequência de 1 ao número do input

def factorial ( num ):
  fat = 1
  for i in range(2,num+1):
    fat = fat * i

  print (fat)

n = int(input())
fat = factorial(n)
