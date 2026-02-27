precoUnitario: float
qtdCompra: int
dinheiroRecebido: float
troco: float
dinheiroInsuficiente: float

precoUnitario = float(input("Preço unitário do produto:"))
qtdCompra = int(input("Quantidade comprada:"))
dinheiroRecebido = float(input("Dinheiro recebido:"))

troco = dinheiroRecebido - (precoUnitario * qtdCompra)
dinheiroInsuficiente = (precoUnitario * qtdCompra) - dinheiroRecebido

if (precoUnitario * qtdCompra) > dinheiroRecebido:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {dinheiroInsuficiente:.2f} REAIS")
else:
    print(f"TROCO = {troco:.2f}")