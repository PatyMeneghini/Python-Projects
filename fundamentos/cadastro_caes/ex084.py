cachorros = []
dados = []
menor = maior = 0
while True:
    dados.append(str(input('Raça: ')).strip())
    dados.append(float(input('Peso: ')))
    cachorros.append(dados[:])
    dados.clear()
    resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{len(cachorros)} cachorros foram cadastrados.')
pesos = [p[1] for p in cachorros]
print(f'O maior peso foi de {max(pesos)}. Peso de ', end= '')
for p in cachorros:
    if p[1] == max(pesos):
        print(f'[{p[0]}]')
print(f'O menor peso foi de {min(pesos)}. Peso de ', end= '')
for p in cachorros:
    if p[1] == min(pesos):
        print(f'[{p[0]}]',end='')