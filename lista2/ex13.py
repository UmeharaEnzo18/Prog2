num = int(input('Digite um numero: '))

for lin in range(1, num+1):
    
    # 1a ou Ultima linha
    if (lin==1 or lin==num):       
        # Imprimir O
        print('*', end='')

        # Imprimir -
        print('*' * num, end='')

        # Imprimir O
        print('*')

    else:        
        # Imprimir O
        print('*', end='')

        # Imprimir -
        print(' ' * num, end='')

        # Imprimir O
        print('*')
