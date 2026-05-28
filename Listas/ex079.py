numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()
    if continuar == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')

