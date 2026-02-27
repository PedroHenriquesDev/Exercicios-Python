qtdMinutos: int
valorPago: float
valorTotal = int
minutosExcedentes = int

qtdMinutos = int(input("Digite a quantidade de minutos:"))

minutosExcedentes = qtdMinutos - 100

minutosExcedentes = minutosExcedentes * 2

valorTotal = minutosExcedentes + 50.00


if qtdMinutos < 100:
    print("Valor a pagar: R$ 50.00 ")
elif qtdMinutos > 100:
    print(f"Valor a pagar: R${valorTotal:.2f}")

