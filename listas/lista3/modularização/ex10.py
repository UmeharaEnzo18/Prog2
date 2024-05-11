base = float(input('Digite a base do triangulo: '))
altura = float(input('Digite a altura do triangulo: '))

def HIPOTENUSA(b, a):
    
    base = b * b
    altura = a * a
    temp = base + altura
    hipotenusa = temp * temp
    
    return hipotenusa

res = HIPOTENUSA(base, altura)

print('A hipotenusa do triangulo é: ', res)