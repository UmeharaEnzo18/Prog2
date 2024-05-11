base = int(input('Digite a base para a exponenciacao: '))
expoente = int(input('Digite o expoente da exponenciacao: '))

def potencia(num1, num2):
    
    base1 = num1
    
    for i in range (1, num2):
        
        num1 = num1 * base1
    
    
    return num1
        
res = potencia(base, expoente)

print('o resultado da potenciacao de base {} e expoente {} é {}'.format(base, expoente, res))