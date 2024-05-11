# num = int(input('digite um numero '))

# def qntDigitos(n1):
#         return len(str(n1))
        
# res = qntDigitos(num)
# print(res)

num = int(input('Digite um numero: '))

def qntDigitos(n1):
    
    digitos = 0
    
    while n1 != 0:
        n1 = n1 // 10
        digitos += 1
            
    return digitos

result = qntDigitos(num)

print(result)