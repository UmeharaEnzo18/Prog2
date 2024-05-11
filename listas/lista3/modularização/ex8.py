x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

def VERIFICA_QUADRANTE(x, y):
    
    if(x > 0 and y > 0):
        return print('Voce se refere ao 1o quadrante')
    
    elif(x < 0 and y > 0):
        return print('Voce se refere ao 2o quadrante')
        
    elif(x < 0 and y < 0):
        return print('Voce se refere ao 3o quadrante')
    
    elif(x > 0 and y < 0):
        return print('Voce se refere ao 4o quadrante')
    
VERIFICA_QUADRANTE(x, y)