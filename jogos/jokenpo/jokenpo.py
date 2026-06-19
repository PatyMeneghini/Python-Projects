from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
whileplay = 1
while whileplay > 0:
    print('\033[1;32m=-=-\033[m' * 15)
    print(' ' * 25, '\033[1;43mJOKENPÔ\033[m')
    print('\033[1;32m=-=-\033[m' * 15)
    computador = randint(0, 2)
    print(""" SUAS OPÇÕES:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")
    jogador = int(input('Qual é a sua jogada: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('\033[1;31m-=\033[m' * 11)
    print('Computador jogou \033[1m{}\033[m'.format(itens[computador]))
    print('Jogador jogou \033[1m{}\033[m'.format(itens[jogador]))
    print('\033[1;31m-=\033[m' * 11)
    if computador == 0: 
        if jogador == 0:
            print('\033[1;33mEMPATE\033[m')
        elif jogador == 1:
            print('\033[1;32mJOGADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[1;31mCOMPUTADOR VENCE\033[m')
        else:
            print('Jogada inválida!')
    elif computador == 1:
        if jogador == 0:
            print('\033[1;31mCOMPUTADOR VENCE\033[m')
        elif jogador == 1:
            print('\033[1;33mEMPATE\033[m')
        elif jogador == 2:
            print('\033[1;32mJOGADOR VENCE\033[m')
        else:
            print('Jogada inválida!')
    elif computador == 2:
        if jogador == 0:
            print('\033[1;32mJOGADOR VENCE\033[m')
        elif jogador == 1:
            print('\033[1;31mCOMPUTADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[1;33mEMPATE\033[m')
        else:
            print('Jogada inválida!')

    whileplay = int(input('1 ou 0: '))
