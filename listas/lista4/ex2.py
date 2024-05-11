def posNeg (num):
    
    lista = []
    lista.append(num)
    
    while num != 0:
        num = int(input('Digite um numero: '))

        if num != 0:
            lista.append(num)
        else:
            print('Lista criada: ',lista)
            
    listaPos = []
    listaNeg = []
    
    i = 0
    j = len(lista)
    
    for i in range(j):
        if lista[i] > 0:
            listaPos.append(lista[i])
        elif lista[i] < 0:
            listaNeg.append(lista[i])
        
    resPos = 0
    resNeg = 0
        
    for i in listaPos:
        resPos += i
    for i in listaNeg:
        resNeg += i
        
    print('\n','Lista positiva' ,listaPos, '\n', 'Resultado: ', resPos)
    print('\n','Lista negativa' ,listaNeg, '\n', 'Resultado: ', resNeg)
    
res = posNeg(int(input('Digite um numero: ')))