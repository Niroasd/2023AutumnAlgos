def main():
    data = int(input())
    calcPositive(data)


def calcPositive(inputVar):
    data = inputVar

    sum = int(data * (data + 1)/2)

    print(f'The sum of the first {data} positive integers is {sum}')

main()