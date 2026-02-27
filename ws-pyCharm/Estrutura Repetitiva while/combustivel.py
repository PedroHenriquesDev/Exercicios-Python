codigo:int
alcool:int
gasolina:int
diesel:int

codigo = int(input('Informe um codigo (1, 2, 3) ou 4 para parar:'))

alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
    codigo = int(input('Informe um codigo (1, 2, 3) ou 4 para parar:'))

    if codigo == 1:
        alcool = alcool + 1
    elif codigo == 2:
        gasolina = gasolina + 1
    elif codigo == 3:
        diesel = diesel + 1
    elif codigo == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool:{alcool}')
        print(f'Gasolina:{gasolina}')
        print(f'Diesel:{diesel}')

