def primo ( num ):
  for i in range(2, num):
    if(num%i == 0):
      return ("nao")
  return ("sim")
  
n = primo(int(input()))
print (n) 
