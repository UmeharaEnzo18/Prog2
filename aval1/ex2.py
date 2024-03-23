#Enzo Umehara - 0040962113026
#Kilbert Silva - 0040972323039

n = int(input('Digite um numero: '))
dobro = (n * 2)

if(n % 2 == 0):
    
    for i in range(0, n, +1):
        
        print(' ' * i, end='')
        print('*' * dobro)
        dobro = dobro - 2
        
    dobro = 2
    
    for i in range(n, 0, -1):
        
        print(' ' * (i-1), end='')
        print('*' * dobro)
        dobro = dobro + 2

else:
    
    for i in range(0, n, +1):
        
        print(' ' * i, end='')
        print('*' * (dobro - 1))
        dobro = dobro - 2
        
    dobro = 3
    
    for i in range(n-1, 0, -1):
        
        print(' ' * (i-1), end='')
        print('*' * dobro)
        dobro = dobro + 2