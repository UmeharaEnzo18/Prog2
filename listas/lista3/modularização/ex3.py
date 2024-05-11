num = int(input('Digite um numero: '))

def primo(n1):
    
    cont = 0
    
    for i in range(1, (n1+1)):
        if n1 % i == 0:
            cont += 1
            
    if cont == 2 or num == 1:
        return print('Eh primo')
    
    else:
        return print('Nao eh primo')
    
res = primo(num)