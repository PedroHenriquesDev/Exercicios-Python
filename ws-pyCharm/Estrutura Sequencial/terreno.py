metroQuadrado: float
comprimento: float
largura: float
area: float
preco: float


largura = float(input("Digite a largura do terreno:"))
comprimento = float(input("Digite o comprimento do terreno:"))
metroQuadrado = float(input("Digite o valor do metro quadrado:"))

area = comprimento * largura
preco = area * metroQuadrado

print(f"Area do terreno = {area}")
print(f"Preco do terreno = {preco}")