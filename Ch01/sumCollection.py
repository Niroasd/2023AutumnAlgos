def main():
    sumCollection()

def sumCollection():
    sum = 0.0
    while(True):
        try:
            data = int(input())
            if(data == 0):
                break
            sum += data
            print(f'The total is now {sum}')
        except(ValueError):
            print(f'That wasn’t a number.')
    print(f'The grand total is {sum}')

main()