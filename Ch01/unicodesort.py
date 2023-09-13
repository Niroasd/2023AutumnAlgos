def main():
    dataInput = input()
    sortChars(dataInput);

def sortChars(input:str):
    temp = []
    data = input

    for x in data:
        temp.append(x)
    temp.sort()

    for x in temp:
        print(x, end="")


main()