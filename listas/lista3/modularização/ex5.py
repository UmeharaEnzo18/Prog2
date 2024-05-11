altura = float(input('Digite sua altura em cm: '))
sexo = input('Digite o seu sexo: ')

def imc(n1, sexo):
    
    #tratamento de altura
    if(n1 > 100):
        n1 /= 100
    
    #tratamento do sexo para a função
    feminino = ['FEMININO','Feminino','Fem','F','feminino','f']
    masculino = ['MASCULINO','Masculino','Masc','M','masculino','m']
    
    if(sexo in feminino):
        return (62.1 * n1) - 44.7
    
    elif(sexo in masculino):
        return (72.7 * n1) - 58
    
    else:
        print('Digite corretamente o sexo')    
    
        
res = imc(altura, sexo)

print('O seu peso ideal eh: {:.2f}'.format(res))