n = int(input("Digite um número: "))



for i in range(1, n + 1):

    asteriscos = '*' * n
    
    print(' ' * (n - i), end=asteriscos)
    
    print(asteriscos)
