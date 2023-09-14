def main():
    data = int(input())
    square_method(data)

def square_method(inputData):
    power = inputData
    newDict = {}

    i = 1

    while(i <= power):
        newDict[i] = (i * i)
        i += 1

    print(f'{newDict}')

main()