def contaNum(num):
    
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
        
    numPos = 0
    numNeg = 0
        
    for i in listaPos:
        numPos += 1
    for i in listaNeg:
        numNeg += 1
        
    print('\n','Soma lista positiva', '\n', 'Resultado: ', numPos)
    print('\n','Soma lista negativa', '\n', 'Resultado: ', numNeg)
    
res = contaNum(int(input('Digite um numero: ')))