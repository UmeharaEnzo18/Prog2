n = int(input("Digite um número: "))
metade = n // 2

a = 0

for i in range(3, 1, -1):
   
   a += 2
   
   if i == 3:
      print(' ' * i, end='')
      print('*')
   
   print(' ' * (i-1), end='')
   print('*' * (a+1))
   
  
if(metade % 2 != 0):
   print(' ', end='')
   print(5 * '*')
    
    
for i in range(1, metade, +1):
  
   a -= 1
   
   if i == 1:
      print(' ' * (i+1), end='')
      print('*' * a)
     
   print(' ' * (i+2), end='') 
   print('*' * (a-2))
