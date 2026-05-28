numeros = []

for i in range(0,5):
     numeros.append(int(input(f'Digite um valor para a posição {i}: ')))

maior_valor = max(numeros)
menor_valor = min(numeros)
print(f'Você digitou os valores {numeros}')

print(f'O maior valor é {maior_valor} nas posições: ', end='')
for i, v in enumerate(numeros):
    if v == maior_valor:
        print(i, end=' ')

print(f'\nO menor valor é {menor_valor} nas posições: ', end='')
for i, v in enumerate(numeros):
    if v == menor_valor:
        print(i, end=' ')



