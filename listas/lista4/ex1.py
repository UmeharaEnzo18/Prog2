def listagem(num):
    
    lista = []
    
    lista.append(num)
    
    while num > 0:
                
            num = int(input('Digite um numero: '))
            
            if num > 0:    
                lista.append(num)
            else:       
                print(lista)

    i = len(lista)

    while i >= len(lista):
        
        print(lista[::-1])
        i -= 1
        
num = int(input('Digite um numero: '))
res = listagem(num)