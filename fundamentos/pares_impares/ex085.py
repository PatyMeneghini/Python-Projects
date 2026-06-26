pares = []
impares = []
for c in range (1,8):
    num=int(input(f'Digite o {c}ª valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('--'*20)
print('Os valores pares digitados foram: ', end='')
print(pares)
print('Os valores impares digitados foram: ', end='')
print(impares)