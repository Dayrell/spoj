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
