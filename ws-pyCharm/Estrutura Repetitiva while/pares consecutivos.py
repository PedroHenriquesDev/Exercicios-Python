x:int
soma:int

x = int(input('Digite um numero inteiro:'))

soma = 0

while x != 0:

    if x % 2 == 0:
        soma = x + (x + 2) + (x + 2 + 2) + (x + 2 + 2 + 2) + (x + 2 + 2 + 2 + 2)
        print(f'SOMA = {soma}')
    elif x % 2 == 1:
        soma = (x + 1) + (x + 1 + 2) + (x + 1 + 2 + 2) + (x + 1 + 2 + 2 + 2) + (x + 1 + 2 + 2 + 2 + 2)
        print(f'SOMA = {soma}')

    x = int(input('Digite um numero inteiro:'))