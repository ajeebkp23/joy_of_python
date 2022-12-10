from base import greetme

greetme('Ajeeb')


while True:
    print('>'*10)
    print('Press q then enter to quit')
    print('Enter your name to greet:')
    print('>'*10)
    name = input('')
    if name == 'q':
        print('Exiting ...')
        break
    greetme(name)
    print('\n'*1)
    print('\n'*3)