# Fábio Dayrell Ferreira Martins Rosa | 2011054383
# Overflow (URI1080)
# Pego a primeira entrada e defino ela como o maior número e o índice igual a 1.
# Pego as demais 99 entradas e para cada uma verifico se ela é maior que o maior
# número definido anteriormente e incremento um contador. Se for maior. essa
# entrada fica como maior número e o index fica sendo o contador.

count = 0
bigger = int(input())
index = 1
while (count < 99):
    count += 1
    number = int(input())
    if (number > bigger):
        bigger = number
        index = count + 1

print(bigger)
print(index)
