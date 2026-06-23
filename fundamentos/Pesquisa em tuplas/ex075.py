Valores = ()
for c in range (0,4):
    num = (int(input('Digite um número: ')))
    Valores += (num,)
procurado = int(input('Qual número deseja pesquisar? '))
print(f'Você digitou os valores {Valores}')
if procurado in Valores:
    print(f'O valor {procurado} apareceu  {Valores.count(procurado)} vezes.')
    print(f'O {procurado} apareceu na {Valores.index(procurado)+1}ª posição.')
else:
    print(f'O valor {procurado} não foi digitado.')
print('Os valores pares digitados foram: ', end='')
par = False
for num in Valores:
    if num % 2 == 0:
        print(num, end=' ')
        par = True
if not par:
    print('Não foram digitados números pares')




