from random import randint
from time import sleep
v = 0
print('\033[32m--\033[m' * 10)
print('\033[1mPAR OU IMPAR?\033[m'.center(25))
print('\033[32m--\033[m' * 10)
while True:
    num = int(input('Digite um valor: '))
    computador = randint(0, 10)
    resultado = num + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print (f'Você jogou {num} e o computador {computador}. Total: {resultado}', end = ' ')
    print('PAR' if resultado % 2 == 0 else 'IMPAR')
    if escolha == 'P':
        if resultado % 2 == 0:
            print('VENCEU!')
            v += 1
        else:
            print('PERDEU!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:
            print('VENCEU!')
            v += 1
        else:
            print('PERDEU!')
            break
    print('De novo...Mais uma jogada!')
    print('...')
    sleep(1)
print('\033[1mGAME OVER\033[m', end = ' ')
sleep(1)
if v == 1:
    print('Você ganhou {} vez'.format(v))
else:
    print('Você ganhou {} vezes'.format(v))