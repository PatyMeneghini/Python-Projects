pares = []
impares = []
for c in range (1,8):
    num=int(input(f'Digite o {c}ª valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('--'*35)
print('Os valores pares digitados foram: ', end='')
pares.sort()
print(pares)
print('Os valores impares digitados foram: ', end='')
impares.sort()
print(impares)
print('--'*35)
# num = [[],[]]
# valor = 0
# for c in range (1,8):
#     valor=int(input(f'Digite o {c}ª valor: '))
#     if valor % 2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)
# print('--'*20)
# num[0].sort()
# num[1].sort()
# print(f'Pares : {num[0]}')
# print(f'Ímpares {num[1]}')