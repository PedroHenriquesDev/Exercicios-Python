from random import randint
numero_aleatorio = (randint(1,10), randint(1,10),
                    randint(1,10), randint(1,10),
                    randint(1,10))

for i in numero_aleatorio:
    print(f'{i} ',end='')

print(f'\nO maior valor sorteado foi {max(numero_aleatorio)}')
print(f'O menor valor sorteado foi {min(numero_aleatorio)}')