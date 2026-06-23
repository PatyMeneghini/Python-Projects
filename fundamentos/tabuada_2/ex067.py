while True:
    num = int(input('\033[1mDigite um valor para saber sua tabuada:\033[m '))
    if num <0:
        break
    print('\033[1;32m==\033[m' * 20)
    cont = 0
    while cont <10:
        cont += 1
        print(f'{num} X {cont} = \033[4m{num*cont}\033[m')
    print('\033[1;32m==\033[m' * 20)
print('FIM')