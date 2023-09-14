def main():
    arithmetic()

def arithmetic():
    data1 = int(input())
    data2 = int(input())
    addition = data1 + data2
    subtraction = data1 - data2
    multiply = data1 * data2
    division = data1/data2
    modulo = data1 % data2
    power = pow(data1, data2)


    print(f'{data1} + {data2} is {addition}')
    print(f'{data1} - {data2} is {subtraction}')
    print(f'{data1} * {data2} is {multiply}')
    print(f'{data1} / {data2} is {division}')
    print(f'{data1} % {data2} is {modulo}')
    print(f'{data1} ^ {data2} is {power}')


main()