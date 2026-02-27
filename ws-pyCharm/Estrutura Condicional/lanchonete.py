codigo: int
qtdComprada: int
valor: float

codigo = int(input("Codigo do produto comprado:"))
qtdComprada = int(input("Quantidade comprada:"))

if codigo == 1:
    valor = 5.00 * qtdComprada
    print(f"Valor a pagar: R${valor:.2f}")
elif codigo == 2:
    valor = 3.50 * qtdComprada
    print(f"Valor a pagar: R${valor:.2f}")
elif codigo == 3:
    valor = 4.80 * qtdComprada
    print(f"Valor a pagar: R${valor:.2f}")
elif codigo == 4:
    valor = 8.90 * qtdComprada
    print(f"Valor a pagar: R${valor:.2f}")
elif codigo == 5:
    valor = 7.32 * qtdComprada
    print(f"Valor a pagar: R${valor:.2f}")
else:
    print("CÓDIGO INVÁLIDO")

