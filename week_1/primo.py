# Fábio Dayrell Ferreira Martins Rosa | 2011054383
# Primo (PRIMO)
# Se o número for divisível por um número x (1 < x < número), ele é primo e
# retorna "não"

def primo ( num ):
  for i in range(2, num):
    if(num%i == 0):
      return ("nao")
  return ("sim")

n = primo(int(input()))
print (n)
