def balao(num):
    cont = 1
    metade = num // 2
    i = 1
    while i < metade:
        str = '*' * cont
        print(str.center(num))
        if cont != metade:
            cont += 2
        i += 1

    i = 1
    while i < metade:
        str = '*' * (metade - 1)
        print(str.center(num))
        metade -= 2
        i = 1

balao(8)