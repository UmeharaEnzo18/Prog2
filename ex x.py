numero = int(input('Digite um numero: '))


for i in range(1, numero + 1):
    espacos = ' ' * (numero - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacos + asteriscos)

