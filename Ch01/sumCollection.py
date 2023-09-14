def main():
    sumCollection()

def sumCollection():
    sum = 0
    while(True):
        try:
            data = int(input())
            if(data == 0):
                break
            sum += data
            print(f'')
        except(ValueError):
            print(f'That wasn’t a number.')
    print(f'{sum}')

main()