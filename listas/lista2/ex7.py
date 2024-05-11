n = int(input('Digite um numero: '))
metade = n // 2

# 1a metade
for i in range(1, metade + 1):
   print(' ' * (i - 1) + '*')

#linha do meio quando impar
if(n % 2 != 0):
    print(metade * ' ' + '*')

# 2a metade
for i in range(metade, 0, -1):
   print(' ' * (i - 1) + '*')
  
