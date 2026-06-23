from random import randint
computador = randint(0, 10)
cont = 0
print('\033[1;35mPensei em um numero entre 0 e 10. \nConsegue adivinhar qual foi?\033[m')
acertou = False
while not acertou:
    jogador = int(input('\033[1;37mQual seu palpite? \033[m'))
    cont += 1
    if  jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('\033[4;36mMenos... Tente mais uma vez\033[m')
        elif jogador < computador:
            print('\033[4;36mMais... Tente mais uma vez\033[m')
print('\033[1;34mAcertou com {} tentativas\033[m'.format(cont))
