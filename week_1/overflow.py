def operation(overflow, equation):
    num1,signal,num2 = equation.split(' ')

    if(signal == '+'):
        total = int(num1) + int(num2)
    elif(signal == '*'):
        total = int(num1) * int(num2)

    if(total > overflow):
        print('OVERFLOW')
    else:
        print('OK')

operation(int(input()), raw_input())
