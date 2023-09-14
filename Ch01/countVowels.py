def main():
    data = input().lower()
    countVowels(data)

def countVowels(inputData: str):
    data = inputData
    dataLength = len(data)
    wovels = ['a', 'e', 'o', 'u', 'i']
    i = 0
    j = 0

    while(j < dataLength):
        if data[j] in wovels:
            i += 1

        j += 1

    print(f'Number of vowels: {i}')

main()