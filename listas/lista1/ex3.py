num = int(input('Digite um numero: '))

for lin in range(1, num):
    print('-' * (num - lin), end='')
    print('*-' * (lin - 1), end='')
    print('*')
