num1 = int(input('Digite um numero para saber o fatorial: '))

def fatorial(n1):
    
    temp = n1
    
    for i in range(1, n1):
        temp *= i
        
    return temp
        
              
res = fatorial(num1)

print('resultado', res)