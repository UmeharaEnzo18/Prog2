num = int(input('Digite a quantidade de segundos: '))

def tempo(segundos):
    
    minutos = 0
    horas = 0
    
    for i in range(0, segundos):
        if segundos >= 60:
            minutos += 1
            segundos -= 60    
        
        if minutos >= 60:
            horas += 1
            minutos -= 60
            
    if segundos < 0:
        segundos = 0
    
    
    print('A fabrica operou por {} hora(s), {} minuto(s) e {} segundo(s)'.format(horas, minutos, segundos))
    
tempo(num)