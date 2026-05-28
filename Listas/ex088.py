from random import randint
lista = []
cont = 0
while True:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
lista.sort()
print(f'Os numeros sorteados foram {lista}')

