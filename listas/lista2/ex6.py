n = int(input("Digite um número: "))

for i in range(n, 0, -1):

    asteriscos = '*' * n
    print(' ' * (n - i), end=asteriscos + '\n')  