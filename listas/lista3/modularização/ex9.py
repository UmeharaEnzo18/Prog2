salario = int(input('Digite o salario: '))
print('4% => 4')
indiceReajuste = float(input('Digite a porcentagem do indice de reajuste: '))

def REAJUSTE(n1, n2):
    
    indicePorc = n2 / 100 * salario
    final = salario + indicePorc
    
    return final

res = REAJUSTE(salario, indiceReajuste)

print('O salario de {} com o reajuste resulta em: {:2f}'.format(salario, res))