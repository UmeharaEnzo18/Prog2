n = int(input('Digite um numero: '))
metade = n // 2

# 1a metade
for i in range(1, n + 1):
   print(' ' * (i - 1) + '*')


# 2a metade
for i in range(n - 1, 0, -1):
   print(' ' * (i - 1) + '*')
  
