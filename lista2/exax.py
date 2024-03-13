num = int(input('Digite um numero: '))
metade = num // 2

# 1a metade
for lin in range(1, num, +1):
    
    # Imprimir -
    print(' ' * (lin-1), end="")

    # Imprimir O
    print('*', end="")

    # Imprimir -
    print('-' * ((lin * 2) - metade), end="")

    # Imprimir O
    print('*')

# Qdo a qtd de linhas for impar
if (num%2 != 0):
    # Imprimir -
    print("-" * (metade), end="")
    # Imprimir O
    print("O")

# 2a metade
for lin in range(metade, 0, -1):
    
    # Imprimir -
    print('-' * (lin-1), end="")

    # Imprimir O
    print('O', end="")

    # Imprimir -
    print('-' * (num - (2*lin)), end="")

    # Imprimir O
    print('O')
