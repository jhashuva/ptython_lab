import random

a = input('Enter player1 name :')
b = input('Enter player2 name: ')
c = input('Enter player3 name: ')
d = input('Enter player4 name :')

while True:
    choice = input('Do you want to play again ?(Yes/No)')
    if choice == 'No':
        break
    rnumber = random.randint(1,5)
    a1 = int(input('Enter number player1: '))
    b1 = int(input('Enter number player2:'))
    c1 = int(input('Enter number player3 :'))
    d1 = int(input('Enter number player 4 :'))

    if rnumber == a1:
        print('{} you got 1 point'.format(a))
    elif rnumber == b1:
        print('{} you got 1 point'.format(b))
    elif rnumber == c1 :
        print('{} you got 1 point'.format(c))
    elif rnumber == d1:
        print('{} you got 1 point'.format(d))
    else:
        print('Computer got 1 point')