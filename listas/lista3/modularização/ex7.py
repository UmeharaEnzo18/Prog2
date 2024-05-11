print('Idade\n')

anos = int(input('Digite quantos anos tens: '))
meses = int(input('Caso saiba digite quantos meses tens: '))
dias = int(input('Caso saiba digite quantos dias tens: '))

def diasVida(anos, meses, dias):
    
    meses = meses + (anos * 12)
    dias = dias + (meses * 30)
    
    return dias

res = diasVida(anos, meses, dias)

print('Sua idade em dias são {} dias'.format(res))