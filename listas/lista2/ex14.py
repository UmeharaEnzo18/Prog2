num = int(input('Digite um numero: '))
metade = num // 2

# 1a metade
for lin in range(1, metade+1):
    
    if lin == 1:
        
        # Imprimir  
        print('*' * (lin-1), end="")

        # Imprimir *
        print('*', end="")

        # Imprimir  
        print('*' * (num - (2*lin)), end="")

        # Imprimir *
        print('*')

    else:
        # Imprimir  
        print(' ' * (lin-1), end="")

        # Imprimir *
        print('*', end="")

        # Imprimir  
        print(' ' * (num - (2*lin)), end="")

        # Imprimir *
        print('*')

# Qdo a qtd de linhas for impar
if (num%2 != 0):
    # Imprimir  
    print(" " * (metade), end="")
    # Imprimir *
    print("*")

# 2a metade
for lin in range(metade, 0, -1):
    
    if lin == 1:
        
        # Imprimir  
        print('*' * (lin-1), end="")

        # Imprimir *
        print('*', end="")

        # Imprimir  
        print('*' * (num - (2*lin)), end="")

        # Imprimir *
        print('*')

    else:
        # Imprimir  
        print(' ' * (lin-1), end="")

        # Imprimir *
        print('*', end="")

        # Imprimir  
        print(' ' * (num - (2*lin)), end="")

        # Imprimir *
        print('*')
