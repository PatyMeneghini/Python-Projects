print('=='*15)
print(f'{'MENU DE CERVEJAS':^30}')
print('=='*15)
cerveja = ('Pilsen',2.50,'Weiss',3.50,'IPA',4.00,'Pale Ale',3.80,'Stout',4.20,'Red Ale',3.90)
for ceva in range(len(cerveja)):
    if ceva % 2 == 0:
        print(f'{cerveja[ceva]:_<25}',end=' ')
    else:
        print(f'€{cerveja[ceva]:>4.2f}')
print('=='*15)
