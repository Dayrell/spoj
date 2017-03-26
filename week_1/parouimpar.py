plays = []
results = []
teste = 1
while True:
    numRounds = int(input())
    if(numRounds == 0):
        break

    players = [ raw_input(), raw_input() ]

    results.append('Teste ' + str(teste))

    for x in range(0, numRounds):
        numbers = raw_input()
        plays.append(numRounds)
        num1,num2 = numbers.split(' ')

        if((int(num1) + int(num2)) % 2 == 0):
            results.append(players[0])
        else:
            results.append(players[1])

    results.append('')
    teste += 1


for winner in results:
    print(winner)
