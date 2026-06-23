from random import randint
minha_tupla = ()
for c in range(0,5):
   num = randint(0,10)
   minha_tupla+= (num,)
maior = minha_tupla[0]
menor = minha_tupla[0]
for num in minha_tupla:
   if num > maior:
      maior = num
   elif num < menor:
        menor = num
print(f'Valores sorteados: {minha_tupla}')
print(f'O menor valor foi {menor}')
print(f'O maior valor foi {maior}')

#from random import randint
#num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
#print(num)
##print(f'O menor valor foi {min(num)}')
#(f'O maior valor foi {max(num)}')