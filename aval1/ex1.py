#Enzo Umehara - 0040962113026
#Kilbert Silva - 0040972323039

n = int(input('Digite um numero: '))

# Primeira parte
for i in range(0, n, +1):
    print('-' * i, end='')
    print('*')
    
if(n % 2 == 0):
    print('-' * i, end='')
    print('*')
            
#Segunda parte
for i in range((n-1), 0, -1):
    print('-' * (i-1), end='')
    print('*')