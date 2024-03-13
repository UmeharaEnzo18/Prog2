n = int(input("Digite um número: "))
metade = n // 2

for i in range(metade, 0, -1):
   print(' ' * i + '*')
   
  
if(n % 2 != 0):
    print(n * '*')
    
for i in range(1, metade + 1):
   print(' ' * i + '*')