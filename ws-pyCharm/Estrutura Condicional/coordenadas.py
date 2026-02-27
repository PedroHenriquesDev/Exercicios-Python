x: float
y: float

x = float(input('Valor de X:'))
y = float(input('Valor de Y:'))

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif y == 0 and x > 0 or x < 0:
    print('Eixo x')
elif x == 0 and y > 0 or y < 0:
    print('Eixo y')
elif x == 0 and y == 0:
    print('Origem')