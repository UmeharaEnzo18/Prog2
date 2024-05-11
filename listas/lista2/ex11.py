n = int(input('Digite um numero: '))

a = (n * 2)


# 1a metade
for i in range(1, n + 1):
    
    a = a - 2

    print(' ' * (i - 1), end='')
    print('*', end='')
    print(' ' * a, end='')
    print('*')

# 2a metade
for i in range(n - 1, 0, -1):
   
    a += 2
   
    
    print(' ' * (i - 1), end='')
    print('*', end='')
    print(' ' * a, end='')
    print('*')