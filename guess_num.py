import random
num=random.randint(1,100)
play=True
while play:
    x=int(input('Key in your guess:'))
    if x>num:
        print(f'Wrong number ! {x} is larger than the answer!')
        print('Please guess again!')
    elif x<num:
        print(f'Wrong number ! {x} is smaller than the answer!')
        print('Please guess again!')
    elif x==num:
        print(f'Yes! the answer is {num}')
        play=False

