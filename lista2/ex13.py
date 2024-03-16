num = int(input('Digite um numero: '))

for lin in range(1, num+1):
    
    # 1a ou Ultima linha
    if (lin==1 or lin==num):       
        # Imprimir *
        print('*', end='')

        # Imprimir 
        print('*' * num, end='')

        # Imprimir *
        print('*')

    else:        
        # Imprimir *
        print('*', end='')

        # Imprimir 
        print(' ' * num, end='')

        # Imprimir *
        print('*')
