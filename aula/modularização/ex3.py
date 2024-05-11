#Sobra da divisao inteira é o numero ao contrario

num = int(input('Digite um numero: '))

def numInverso(n1):
    
    resto = 0
    
    while n1 != 0:
        resto = n1 % 10
        n1 = n1 // 10
        print(resto, end='')
        
res = numInverso(num)

print(res)