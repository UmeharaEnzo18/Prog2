num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = int(input("Digite outro número inteiro: "))

def mmc(n1, n2, n3):

    if num1 >= num2 and num1 >= num3:
        maior = num1
        
    elif num2 >= num1 and num1 >= num3:
        maior = num2
        
    else:
        maior =  num3

    for i in range(maior):
        temp = num1 * i
        if (temp % num2 and temp % num3) == 0:
            mmc = temp
            print(mmc)

    return mmc

res = mmc(num1, num2, num3)

print('O MMC entre os numeros, {}, {}, {} eh {}'.format(num1, num2, num3, res))

# não funcionando corretamente