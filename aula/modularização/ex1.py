a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

def maiorNumero(a, b, c): # Função para definição do maior numero dos inputs
    
    if a >= b and a >= c:
        return a
    
    elif b >= a and a >= c:
        return b
    
    else:
        return c

maior = maiorNumero(a, b, c)


def dobrar(n1): # Função de dobrar o maior numero anterior
    return n1 * n1

dobro = dobrar(maior)

print('O maior numero eh: {} e o dobro eh: {}'.format(maior, dobro))