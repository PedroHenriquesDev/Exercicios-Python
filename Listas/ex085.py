numeros = []
pares = []
impares = []

for n in range(0, 7):
    num = int(input('Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
