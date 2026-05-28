numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar?[S/N]')).strip().upper()
    if continuar in 'Nn':
        break
print(numeros)
print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')