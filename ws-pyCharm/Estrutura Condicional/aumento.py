salario:float
novoSalario:float
aumento:float
porcentagem:float

salario = float(input('Digite o salario da pessoa:'))

if salario <= 1000.00:
    novoSalario = salario * 1.20
    porcentagem = 20
elif salario > 1000.00 and salario <= 3000.00:
    novoSalario = salario * 1.15
    porcentagem = 15
elif salario > 3000.00 and salario <= 8000.00:
    novoSalario = salario * 1.10
    porcentagem = 10
else:
    salario = salario * 1.05
    porcentagem = 5

print(f'Novo salario = R$ {novoSalario:.2f}')

aumento = novoSalario - salario

print(f'Aumento = R${aumento:.2f}')

print(f'Porcentagem = {porcentagem}%')

