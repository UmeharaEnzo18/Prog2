num = int(input('Digite um numero: '))

for lin in range(1, num + 1):

    print('-' * (lin - 1), end='')
    print('*-' * (num - lin), end='')
    print('*')
    