pessoas = []
dados = []
num_pessoas = 0


while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))

    pessoas.append(dados[:])

    # Atualizando maior e menor peso
    if num_pessoas == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    dados.clear()
    num_pessoas += 1

    continuar = str(input('Deseja continuar?[S/N]')).strip().upper()
    if continuar == 'N':
        break

print(f'O número de pessoas digitadas foi {num_pessoas}')
print(f'O maior peso é {maior_peso}')
print(f'O menor peso é {menor_peso}')