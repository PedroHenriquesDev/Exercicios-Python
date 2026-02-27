precoProduto: float
qtdCompra: int
dinheiroRecebido: float
troco: float

precoProduto = float(input("Preço unitário do produto:"))

qtdCompra = int(input("Quantidade comprada:"))

dinheiroRecebido = float(input("Dinheiro recebido:"))

troco = dinheiroRecebido - (precoProduto * qtdCompra)

print(f"TROCO = {troco}")