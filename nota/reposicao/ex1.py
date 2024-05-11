#Enzo Umehara - 0040962113026
#Kilbert Silva - 0040972323039

num = int(input("Digite um numero: "))
cont = (num * 2) - 2

for i in range(num):
    
    for j in range(num):
        print('-' * i, end='')
        print('*', end='')
        print('-' * (cont - (i * 2)), end='')
        print('*', end='')
        print('-' * i, end='')
    
    print('')